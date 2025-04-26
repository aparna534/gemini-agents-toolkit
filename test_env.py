import os
from dotenv import load_dotenv
import sys
sys.path.append('/Users/Aparna/gemini-agents-toolkit/venv/lib/python3.13/site-packages')

try:
    from dotenv import load_dotenv
    print("dotenv is successfully imported!")
except ImportError as e:
    print("Error importing dotenv:", e)


load_dotenv() 

api_key = os.getenv('API_KEY')
default_model = os.getenv('DEFAULT_MODEL')

print("API_KEY:", api_key)
print("DEFAULT_MODEL:", default_model)
