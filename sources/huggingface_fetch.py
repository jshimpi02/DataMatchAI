import requests

def search_huggingface(query):
    """
    Searches Hugging Face Hub for datasets related to the query.
    """
    print("Searching Hugging Face for:", query)
    url = f"https://huggingface.co/api/datasets?search={query}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        datasets = res.json()[:3]
        return [
            {
                "Dataset": ds["id"],
                "Source": f"https://huggingface.co/datasets/{ds['id']}",
                "Reason": "Matches your research query",
                "Type": ds.get("cardData", {}).get("task_categories", ["N/A"])[0]
            }
            for ds in datasets
        ]
    except Exception as e:
        print("Hugging Face fetch error:", e)
        return []
