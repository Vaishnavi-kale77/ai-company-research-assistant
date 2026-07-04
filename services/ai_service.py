import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


def analyze_company(content, model):

    prompt = f"""
    Analyze this company information.

    Generate:

    1. Company Summary
    2. Products and Services
    3. AI Generated Pain Points
    4. Competitor Companies

    Company Content:
    {content}
    """

    response = requests.post(

        url="https://openrouter.ai/api/v1/chat/completions",

        headers={

            "Authorization":
            f"Bearer {OPENROUTER_API_KEY}",

            "Content-Type":
            "application/json"
        },

        json={

            "model": model,

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]