# Exercise 4 — Semantic Retrieval System

Build a retrieval pipeline that embeds document chunks into a Chroma vector store and retrieves the most relevant passages for natural language queries.

## What It Does

1. Loads the LangChain docs introduction page via `WebBaseLoader`
2. Splits the content into 500-character chunks with `RecursiveCharacterTextSplitter`
3. Embeds all chunks using OpenAI's `text-embedding-3-small` model
4. Stores the embeddings in a local in-memory **Chroma** vector store
5. Creates a retriever that returns the top-3 most similar chunks per query
6. Tests the retriever with 3 sample queries and prints the results

## Key Concepts

- **`OpenAIEmbeddings`** — converts text chunks into dense vector representations using `text-embedding-3-small`
- **`Chroma`** — lightweight local vector database; `from_documents()` embeds and indexes chunks in one call
- **`VectorStoreRetriever`** — wraps the vector store; `invoke(query)` performs a cosine similarity search and returns the top-k chunks
- **`USER_AGENT`** — loaded from `.env` and set before LangChain imports to suppress `WebBaseLoader` warnings

## Pipeline

```
WebBaseLoader → RecursiveCharacterTextSplitter → OpenAIEmbeddings → Chroma → Retriever → Query results
```

## Sample Queries

```
"What is LangChain?"
"How do retrievers work?"
"Why is document splitting important?"
```

## Run

```bash
python 04-semantic-retrieval/retrieval-models.py
```

## Things to Try

- Swap `WebBaseLoader` for `PyPDFLoader` to retrieve from a PDF instead
- Increase `k` in `search_kwargs` to return more results per query
- Persist the Chroma store to disk with `persist_directory` to avoid re-embedding on every run
- Replace `text-embedding-3-small` with `text-embedding-3-large` for higher accuracy
