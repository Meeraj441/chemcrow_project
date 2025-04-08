# 🧪 ChemCrow Project (Local Setup on Windows)

This project sets up [ChemCrow](https://github.com/ur-whitelab/chemcrow) on your local Windows machine, allowing you to use powerful chemical reasoning with AI.

## 📁 Project Structure

```
chemcrow_project/
│
├── main.py            # Python file to run ChemCrow with a prompt
├── .gitignore         # Prevents uploading your environment and secrets
├── requirements.txt   # All necessary Python packages
└── README.md          # This file
```

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chemcrow_project.git
cd chemcrow_project
```

### 2. Create a Virtual Environment (Windows)

```bash
python -m venv chemcrow_env
chemcrow_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

Create a `.env` file in the root directory with this format:

```
OPENAI_API_KEY=your_openai_key_here
SERPAPI_API_KEY=your_serpapi_key_here
```

### 5. Run the App 🎉

```bash
python main.py
```

You should see ChemCrow respond to the prompt inside `main.py`.

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