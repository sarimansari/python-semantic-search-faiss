import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, docs):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.docs = docs
        self.embeddings = self.model.encode(docs).astype("float32")
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query, k=2):
        query_emb = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_emb, k)
        results = [self.docs[i] for i in indices[0]]
        return results
