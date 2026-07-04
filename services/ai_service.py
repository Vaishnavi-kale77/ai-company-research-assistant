import requests
import streamlit as st


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

    headers = {
        "Authorization":
        f"Bearer {st.secrets['OPENROUTER_API_KEY']}",

        "Content-Type":
        "application/json"
    }

    payload = {

        "model": model,

        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    result = response.json()

    if "choices" in result:

        return result["choices"][0]["message"]["content"]

    elif "error" in result:

        return f"API Error: {result['error']}"

    else:

        return f"Unexpected Response: {result}"