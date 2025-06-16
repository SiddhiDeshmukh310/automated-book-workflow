import requests

def review_text(original, rewritten):
    prompt = f"""Compare the original and rewritten texts. Provide feedback on clarity, grammar, and how well the meaning is preserved.

Original:
{original}

Rewritten:
{rewritten}

Give your review below:"""

    payload = {
        "model": "mistral",
        "messages": [
            {"role": "system", "content": "You are a reviewer that evaluates rewritten content."},
            {"role": "user", "content": prompt}
        ],
        "stream": False,  # ✅ required to avoid broken JSON
        "temperature": 0.7
    }

    response = requests.post("http://localhost:11434/api/chat", json=payload)

    try:
        result = response.json()
        return result['message']['content']
    except Exception as e:
        print("⚠️ Failed to decode JSON. Raw response:\n", response.text)
        raise e
