import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")


def search_company(company_name):

    url = "https://google.serper.dev/search"

    payload = {
        "q": f"{company_name} official company website"
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    data = response.json()

    organic_results = data.get("organic", [])

    blocked_domains = [
        "wikipedia.org",
        "linkedin.com",
        "facebook.com",
        "instagram.com",
        "twitter.com",
        "x.com",
        "youtube.com"
    ]

    filtered_links = []

    for result in organic_results:

        link = result.get("link", "")

        if not any(domain in link for domain in blocked_domains):
            filtered_links.append(link)

    if filtered_links:
        return filtered_links[0]

    return "Website not found"