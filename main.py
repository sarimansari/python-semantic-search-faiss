from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever

# Load documents
with open("data/docs.txt") as f:
    docs = [line.strip() for line in f if line.strip()]

retriever = Retriever(docs)
app = FastAPI(title="Semantic Search API")

class QueryRequest(BaseModel):
    query: str
    k: int = 2

@app.post("/search")
def search(request: QueryRequest):
    results = retriever.search(request.query, k=request.k)
    return {"query": request.query, "results": results}
