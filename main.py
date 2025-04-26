import os
from config.settings import PROJECT_ID, REGION, SIMPLE_MODEL, LLM_PROVIDER

if LLM_PROVIDER == "gemini":
    from clients.gemini_client import GeminiClient as LLMClient
else:
    raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")

def main():
    print("Current Directory:", os.getcwd())
    print("Project ID:", PROJECT_ID)
    print("Region:", REGION)
    print("Simple Model:", SIMPLE_MODEL)
    print("LLM Provider:", LLM_PROVIDER)

    client = LLMClient()
    prompt = "How are you today?"
    response = client.generate(prompt)

    print("\nLLM Response:")
    print(response)

if __name__ == '__main__':
    main()

