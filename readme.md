# 🧪 ChemCrow Project (Azure OpenAI)

This project sets up [ChemCrow](https://github.com/ur-whitelab/chemcrow) on your local Windows machine, allowing you to use powerful chemical reasoning with AI.

This version integrates ChemCrow with **Azure OpenAI** using `.env` for secure key management.

The prompt output will be saved in outputs folder with prompt and timestamp as markdown file name.

## 📁 Project Structure

```
chemcrow_project_azure_env/
├── main.py            # Main script to run ChemCrow
├── .env               # Store your Azure API keys (excluded from Git)
├── .gitignore         # Excludes .env and environment folders
├── requirements.txt   # Dependencies
└── README.md          # Setup guide
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<yourusername>/chemcrow_project.git
cd chemcrow_project
```

### 2. Create & Activate Virtual Environment (Windows)

```bash
python -m venv chemcrow_env
chemcrow_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Update `.env` File

Open `.env` and add your Azure details:

```
AZURE_OPENAI_API_KEY=your-azure-api-key
AZURE_OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-05-15
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

### 5. Run the Project

```bash
python main.py
```

---

## 🧪 Sample Prompts You Can Try

You can edit `main.py` and change the prompt:

```python
prompt = "What is the IUPAC name of aspirin?"
```

Other example prompts:
- "Suggest a synthesis route for paracetamol."
- "What is the logP value of caffeine?"
- "Give me the SMILES for acetaminophen."

## ❗ Requirements

- Python 3.10+ (64-bit)
- Internet connection
- Valid OpenAI and SerpAPI keys

## 📌 Dependencies (Pinned in `requirements.txt`)

- `chemcrow`
- `langchain==0.0.275`
- `pydantic==1.10.13`
- `numexpr==2.8.4`
- `numpy<2.0`
- `rdkit-pypi`
- `python-dotenv`

## ⚠️ Notes

- This version is tailored for **Windows compatibility**
- ChemCrow may update and require changes to dependencies in the future

## 🧑‍💻 Maintainer

- **Meeraj Raghunathan** — feel free to fork, extend, and experiment!

## 🧬 Credits

- [ChemCrow on GitHub](https://github.com/ur-whitelab/chemcrow)
- [LangChain](https://github.com/langchain-ai/langchain)
- [RDKit](https://www.rdkit.org/)

---

⚠️ **Never share your `.env` file or commit it to GitHub.** It's already excluded via `.gitignore`.