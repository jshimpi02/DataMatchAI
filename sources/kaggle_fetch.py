import requests

def search_kaggle(query):
    """
    Simulated search for datasets on Kaggle.
    Replace with real API call if authenticated access is available.
    """
    print("Searching Kaggle for:", query)
    return [
        {
            "Dataset": "COVID-19 Open Research Dataset",
            "Source": "https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge",
            "Reason": "Large-scale dataset of scholarly articles about COVID-19",
            "Type": "Medical, NLP"
        }
    ]
