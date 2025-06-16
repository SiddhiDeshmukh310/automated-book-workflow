import requests

def rewrite_text(input_text: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": f"Rewrite the following text in a more polished and professional manner:\n\n{input_text}",
                "stream": False
            }
        )
        result = response.json()
        return result.get("response", "⚠️ Rewrite failed: No response received.")
    except Exception as e:
        return f"⚠️ Rewrite failed due to request error: {e}"
