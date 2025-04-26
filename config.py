import os
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = {
    'google': 'gemini',  
    'openai': 'gpt-3',  
}

DEFAULT_PROVIDER = 'google'

API_KEYS = {
    'google': os.getenv('GOOGLE_API_KEY'),
    'openai': os.getenv('OPENAI_API_KEY'),
}

DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gpt-3')  

