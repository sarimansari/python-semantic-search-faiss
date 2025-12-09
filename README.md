# Python Semantic Search with FAISS

This project demonstrates a simple semantic search API using FastAPI, Sentence Transformers, and FAISS for efficient vector search.

## Features
- Semantic search over a small document set
- REST API with FastAPI
- Uses sentence-transformers for embeddings
- Uses FAISS for fast similarity search

## Setup

### 1. Clone the repository
```
git clone <repo-url>
cd python-semantic-search-faiss
```

### 2. Create and activate a virtual environment (recommended)
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

## Running the API
Start the FastAPI server with Uvicorn:
```
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Usage
Send a POST request to `/search` with a JSON body:
```json
{
  "query": "Apple company",
  "k": 2
}
```

## File Overview
- `main.py`: FastAPI app and API endpoint
- `retriever.py`: Semantic search logic using FAISS and sentence-transformers
- `data/docs.txt`: Sample documents
- `requirements.txt`: Python dependencies
