from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
from dotenv import load_dotenv
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os

class QueryRequest(BaseModel):
    question:str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/query")
async def research_query(query:QueryRequest):
    try:
        graph = GraphBuilder(model_provider="openai")
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("react_graph.png","wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        messages={"messages": [query.question]}
        output = react_app.invoke(messages)

        # If result is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)
        
        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})





