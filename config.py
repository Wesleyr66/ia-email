from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")