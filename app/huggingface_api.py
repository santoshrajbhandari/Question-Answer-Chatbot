import requests
from app.config import HUGGINGFACE_TOKEN, API_URL

headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def query_huggingface(question: str, context: str) -> str:
    payload = {"inputs": {"question": question, "context": context}}
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    return result.get("answer", "I don't know.")
