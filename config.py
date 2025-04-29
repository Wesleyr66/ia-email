from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")