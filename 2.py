import requests
from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

response = ollama.chat.completions.create(
    model="llama3", messages=[
        {"role": "system", "content": "You are a helpful assistant."}])

print(response.choices[0].message.content)