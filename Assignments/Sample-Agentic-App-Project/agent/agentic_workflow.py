from util.model_loader import ModelLoader


class GraphBuilder():
    def __init__(self,model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()

    def __call__(self):
        return self.build_graph()