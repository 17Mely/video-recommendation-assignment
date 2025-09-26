import os, requests, pandas as pd, time
from dotenv import load_dotenv

load_dotenv()
API_BASE = os.environ.get("API_BASE", "https://api.socialverseapp.co")
FLIC_TOKEN = os.environ.get("FLIC_TOKEN")

HEADERS = {"Flic-Token": FLIC_TOKEN}

def fetch_data(endpoint):
    url = f"{API_BASE}{endpoint}"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    posts = fetch_data("/posts")   # replace with actual endpoints
    pd.DataFrame(posts).to_csv("data/posts.csv", index=False)
