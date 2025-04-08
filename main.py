from chemcrow import ChemCrow
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

def main():
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("SERP_API_KEY"):
        print("⚠️ Please set your API keys in the .env file.")
        return
    agent = ChemCrow()
    agent.run("What is phenol?")

if __name__ == "__main__":
    main()
