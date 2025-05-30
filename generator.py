# generator.py — Dataset suggestion backend using Hugging Face Inference API
import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def query_suitable_datasets(research_goal):
    prompt = f"""
You are a research assistant. Given the research goal: "{research_goal}", suggest 3-5 public datasets that could be used for this research.
For each dataset, provide:
- Dataset Name
- Link or source
- Why it's suitable (1-2 lines)
- Domain/Type (e.g., medical, NLP, time series, image)
Return a structured JSON list like this:
[
  {{"Dataset": "...", "Source": "...", "Reason": "...", "Type": "..."}},
  ...
]
"""
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.6,
            "max_new_tokens": 512,
            "return_full_text": False
        }
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        output = response.json()[0]["generated_text"]
        return eval(output.strip())
    except Exception as e:
        print("Dataset suggestion failed:", e)
        return []
