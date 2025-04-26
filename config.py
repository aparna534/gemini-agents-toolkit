import os
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = {
    'google': 'gemini',  # You can replace this with your specific model from Gemini
    'openai': 'gpt-3',  # For OpenAI GPT models
}

DEFAULT_PROVIDER = 'google'

API_KEYS = {
    'google': os.getenv('GOOGLE_API_KEY'),
    'openai': os.getenv('OPENAI_API_KEY'),
}

DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gpt-3')  # Default to 'gpt-3' or your desired model

