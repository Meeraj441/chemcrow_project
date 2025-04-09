import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from chemcrow.agents.chemcrow import ChemCrow

# ✅ Patch ChemCrow to inject custom llm
class PatchedChemCrow(ChemCrow):
    def __init__(self, llm):
        # Bypass original __init__ that expects OPENAI_API_KEY
        self.llm = llm
        self.tools = []  # Optional: could load tools later if needed

    def run(self, prompt: str):
        return self.llm.invoke(prompt)

def main():
    load_dotenv()

    # ✅ Azure LLM setup
    llm = AzureChatOpenAI(
        openai_api_type="azure",
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0.7
    )

    # ✅ Use patched ChemCrow
    agent = PatchedChemCrow(llm=llm)

    prompt = "What are the common methods used in manufacturing paracetamol in a research setting?"
    response = agent.run(prompt)

    print("\n🧪 ChemCrow Response:\n", response)

if __name__ == "__main__":
    main()
