from util.model_loader import ModelLoader
from langgraph.graph import MessagesState,StateGraph,END,START
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.types import Command
from message.app_message import AgentState
from prompt.app_prompt import SYSTEM_ROUTER_PROMPT,SYSTEM_REPORT_PROMPT,SYSTEM_RESEARCH_PROMPT,SYSTEM_FINNACIAL_RESEARCH,SYSTEM_PHARMA_RESEARCH
from domain.app_router import Router
from typing import Literal
from langgraph.prebuilt import create_react_agent
from tool.search_tool import SearchTool

class GraphBuilder():
    def __init__(self,model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        self.search_tool=SearchTool

    def supervisor_agent(self,state:AgentState)->Command[Literal['research_supervisor', 'reporting_supervisor', '__end__']]:
        messages = [{"role": "system", "content": SYSTEM_ROUTER_PROMPT},] + state["messages"]
        llm_with_structure_output=self.llm.with_structured_output(Router)
        response=llm_with_structure_output.invoke(messages)
        goto=response["next"]
        print("**********BELOW IS MY GOTO***************")
        print(goto)
        if goto == "FINISH":
            goto="__end__"
        return Command(goto=goto, update={"next":goto})
    
    def research_supervisor(self,state:AgentState)->Command[Literal['pharma_research', 'financial_research', 'supervisor']]:
        messages = [{"role": "system", "content": SYSTEM_RESEARCH_PROMPT},] + state["messages"]
        llm_with_structure_output=self.llm.with_structured_output(Router)
        response=llm_with_structure_output.invoke(messages)
        goto=response["next"]
        print("**********BELOW IS MY GOTO***************")
        print(goto)
        if goto == "FINISH":
            goto="__end__"
        return Command(goto=goto, update={"next":goto})

    def pharma_research_agent(self,state:AgentState)->Command[Literal['research_supervisor']]:

        research_agent = create_react_agent(self.llm, tools=[self.search_tool], prompt=SYSTEM_PHARMA_RESEARCH)
            
        result=research_agent.invoke(state)

        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="pharma_research")
                ]
            },
            goto="research_supervisor",
        )

    def financial_research_agent(self,state:AgentState)->Command[Literal['research_supervisor']]:
        research_agent = create_react_agent(self.llm, tools=[self.search_tool], prompt=SYSTEM_FINNACIAL_RESEARCH)
            
        result=research_agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="financial_research")
                ]
            },
            goto="research_supervisor",
        )


    def reporting_supervisor(self,state:AgentState)->Command[Literal['report_creator', 'document_generator', 'supervisor']]:
        messages = [{"role": "system", "content": SYSTEM_REPORT_PROMPT},] + state["messages"]
        llm_with_structure_output=self.llm.with_structured_output(Router)
        response=llm_with_structure_output.invoke(messages)
        goto=response["next"]
        print("**********BELOW IS MY GOTO***************")
        print(goto)
        return Command(goto=goto, update={"next":goto})


    def report_creator_agent(state:AgentState)->Command[Literal['reporting_supervisor']]:

        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="report_creator")
                ]
            },
            goto="reporting_supervisor",
        )

    def document_generator_agent(state:AgentState)->Command[Literal['reporting_supervisor']]:

        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="document_generator")
                ]
            },
            goto="reporting_supervisor",
        )
    
    def build_graph(self):
        a2a_graph = StateGraph(AgentState)

        a2a_graph.add_node("supervisor",self.supervisor_agent)
        a2a_graph.add_node("research_supervisor",self.research_supervisor)
        a2a_graph.add_node("pharma_research",self.pharma_research_agent)
        a2a_graph.add_node("financial_research",self.financial_research_agent)

        a2a_graph.add_node("reporting_supervisor",self.reporting_supervisor)
        a2a_graph.add_node("report_creator",self.report_creator_agent)
        a2a_graph.add_node("document_generator",self.document_generator_agent)

        a2a_graph.set_entry_point("supervisor")

        a2a_app=a2a_graph.compile()
        return a2a_app


    def __call__(self):
        return self.build_graph()