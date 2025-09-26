from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/feed")
def get_feed(username: str, limit: int = 10):
    # Load collected data (replace with your recommender logic)
    posts = pd.read_csv("data/posts.csv")
    recs = posts.head(limit).to_dict(orient="records")
    return {"username": username, "recommendations": recs}
