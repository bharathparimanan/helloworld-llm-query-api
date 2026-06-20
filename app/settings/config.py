import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
model = os.getenv("ANTHROPIC_MODEL_IDENTIFIER")