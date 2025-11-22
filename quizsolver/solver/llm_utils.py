import requests
from config import USE_AIPIPE, AIPIPE_API_KEY, OPENAI_API_KEY
print(USE_AIPIPE)
def query_llm(prompt: str) -> str:
    if USE_AIPPIPE:
        headers = {"Authorization": f"Bearer {AIPIPE_API_KEY}"}
        payload = {"model": "gpt-4o-mini", "prompt": prompt, "max_tokens": 500}
        res = requests.post("https://api.aipipe.ai/v1/completions", json=payload, headers=headers)
        return res.json()["choices"][0]["text"].strip()
    else:
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
        payload = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}
        res = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
        return res.json()["choices"][0]["message"]["content"].strip()