import requests
import streamlit as st


def analyze_company(content, model):

    prompt = f"""
    Analyze this company information and provide:

    1. Company Summary
    2. Products and Services
    3. AI Generated Pain Points
    4. Competitor Companies

    Website Content:
    {content}
    """

    headers = {
        "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
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

    print(result)

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    elif "error" in result:
        return f"API Error: {result['error']}"

    else:
        return "Unknown error occurred."