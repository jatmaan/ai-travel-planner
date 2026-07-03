import requests
from prompts import SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ai(user_prompt):
    full_prompt = SYSTEM_PROMPT + "\n\nUser request: " + user_prompt

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": full_prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]