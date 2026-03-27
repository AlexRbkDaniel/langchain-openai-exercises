import os

from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("USER_AGENT", os.getenv("USER_AGENT", "smart-ai-apps-playground/1.0"))

from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load a document about AI
loader = WebBaseLoader("https://python.langchain.com/v0.2/docs/introduction/")
documents = loader.load()

# 2. Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# 3. Set up the embedding model
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
)

# 4. Create a vector store
vector_store = Chroma.from_documents(chunks, embedding=embedding_model)

# 5. Create a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})


# 6. Define a function to search for relevant information
def search_documents(query, top_k=3):
    """Search for documents relevant to a query"""
    docs = retriever.invoke(query)
    return docs[:top_k]


# 7. Test with a few queries
test_queries = [
    "What is LangChain?",
    "How do retrievers work?",
    "Why is document splitting important?"
]

for query in test_queries:
    print(f"\nQuery: {query}")
    results = search_documents(query)
    for i, doc in enumerate(results, 1):
        print(f"  Result {i}: {doc.page_content[:200]}...")
