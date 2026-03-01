import requests
from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")


# Model response using llama3 model with a simple prompt.
response = ollama.chat.completions.create(
    model="llama3", messages=[
        {"role": "user", "content": "Tell me a fun fact."}])

print(response.choices[0].message.content)
