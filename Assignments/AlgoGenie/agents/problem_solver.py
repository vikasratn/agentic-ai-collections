from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client
from prompt.system_prompt import get_system_message


model_client = get_model_client()
system_message = get_system_message()

def get_problem_solver_agent():
    """
    Function to get the problem solver agent.
    This agent is responsible for solving DSA problems.
    It will work with the code executor agent to execute the code.
    """
    problem_solver_agent = AssistantAgent(
            name="DSA_Problem_Solver_Agent",
            description="An agent that solves DSA problems",
            model_client=model_client,
            system_message=system_message
        )
    
    return problem_solver_agent