import os
from dotenv import load_dotenv
from chemcrow import ChemCrow
from langchain.chat_models import AzureChatOpenAI

def main():
    load_dotenv()  # Load environment variables from .env

    llm = AzureChatOpenAI(
        openai_api_type="azure",
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0.7
    )

    agent = ChemCrow(llm=llm)
    prompt = "Suggest a synthesis route for paracetamol."
    response = agent.run(prompt)

    print("\n🧪 ChemCrow Response:\n", response)

if __name__ == "__main__":
    main()