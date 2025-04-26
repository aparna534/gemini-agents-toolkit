from clients.base_client import BaseClient
import google.generativeai as genai
from config.settings import SIMPLE_MODEL

class GeminiClient(BaseClient):
    def __init__(self):
        self.model = genai.GenerativeModel(model_name=SIMPLE_MODEL)

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

