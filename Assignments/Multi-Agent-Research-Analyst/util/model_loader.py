import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from util.config_loader import ConfigLoader
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


class ModelLoader(BaseModel):
    model_provider: Literal["openai","groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None,exclude=True)

    def model_post_init(self,__context:Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        provider = self.model_provider.lower()
        print(f"Loading model from provider: {provider}")
        load_dotenv()
        if provider == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            print("Loading LLM from Groq...")
            return ChatGroq(model=model_name, api_key=api_key)
        elif provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            print("Loading LLM from OpenAI...")
            return ChatOpenAI(model_name=model_name, api_key=api_key)
        else:
            raise ValueError(f"Unsupported model provider: {provider}")





    
