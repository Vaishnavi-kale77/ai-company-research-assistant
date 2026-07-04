import requests
import streamlit as st


OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]


def analyze_company(content, model):

    prompt = f"""
    Analyze this company website content.

    Provide:
    1. Company Summary
    2. Products and Services
    3. AI Generated Pain Points
    4. Competitor Companies

    Website Content:
    {content[:4000]}
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
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
        json=data
    )

    result = response.json()

    # DEBUG ERROR HANDLING
    if "choices" not in result:

        return f"""
        API Error:

        {result}
        """

    return result["choices"][0]["message"]["content"]