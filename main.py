from chemcrow import ChemCrow
from langchain.chat_models import AzureChatOpenAI

def main():
    llm = AzureChatOpenAI(
        openai_api_type="azure",
        openai_api_key="<your-azure-api-key>",
        openai_api_base="https://<your-resource-name>.openai.azure.com/",
        openai_api_version="2023-05-15",
        deployment_name="gpt-4o",
        temperature=0.7
    )

    agent = ChemCrow(llm=llm)
    prompt = "Suggest a synthesis route for paracetamol."
    response = agent.run(prompt)

    print("\n🧪 ChemCrow Response:\n", response)

if __name__ == "__main__":
    main()
