import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
TOKEN = os.getenv("HUGGINGFACE_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"}

def query(question, context):
    payload = {"inputs": {"question": question, "context": context}}
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return "Model error"

    return response.json().get("answer")

question = "What does Hugging Face provide?"
context = "Hugging Face is a company that provides open-source tools for natural language processing tasks."

print("Answer:", query(question, context))
