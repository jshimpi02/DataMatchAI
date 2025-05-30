# sources/pwc_fetch.py
import requests

def search_pwc(query):
    """
    Searches PapersWithCode for datasets related to a research query.
    """
    print("Searching PapersWithCode for:", query)
    url = f"https://paperswithcode.com/api/v1/search/?q={query}"
    headers = {"Accept": "application/json"}
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        papers = res.json().get("results", [])[:3]
        return [
            {
                "Dataset": p.get("paper_title", "Unknown Paper"),
                "Source": p.get("url_abs", "https://paperswithcode.com"),
                "Reason": "Related paper with linked dataset or benchmark",
                "Type": "ML/NLP"
            }
            for p in papers
        ]
    except Exception as e:
        print("PWC fetch error:", e)
        return []
