@echo off
echo Creating virtual environment...
python -m venv chemcrow_env

echo Activating environment...
call chemcrow_env\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo 🔑 SET your OpenAI and SERP API keys in the environment manually or here.
echo Example:
echo set OPENAI_API_KEY=your-key-here
echo set SERP_API_KEY=your-serpapi-key-here

pause
