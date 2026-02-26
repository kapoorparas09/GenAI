# In terminal run ollama server and then run this script to test if the server is running properly.
import requests

response = requests.get("http://localhost:11434/").content
print(response)