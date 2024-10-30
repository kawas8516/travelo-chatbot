import requests
import os

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HUGGINGFACE_API_TOKEN = os.getenv("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")

def query_huggingface(prompt):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": "Failed to get response from Hugging Face API"}
