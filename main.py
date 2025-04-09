import os
import re
from datetime import datetime
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

# ✅ Create a safe filename from a prompt
def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # remove special chars
    text = re.sub(r"[\s]+", "_", text)    # replace spaces with underscores
    return text.strip("_")

def save_response_to_md(prompt: str, response_text: str, output_dir="outputs"):
    # Generate safe filename using the prompt
    filename_slug = slugify(prompt)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_slug}_{timestamp}.md"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    # Format markdown content
    md_content = f"""# 🧪 ChemCrow Response

**Prompt:** `{prompt}`

---

{response_text}
"""

    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"\n✅ Markdown file saved: {filepath}")


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

    prompt = "What are the common methods used in manufacturing paracetamol in research setting?"
    response = agent.run(prompt)

    print("\n🧪 ChemCrow Response:\n")
    print(response.content)
    save_response_to_md(prompt, response.content)

if __name__ == "__main__":
    main()
