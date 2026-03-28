# Smart AI Apps Playground

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

An educational Python playground for learning to build AI applications using LangChain and OpenAI. Each exercise demonstrates a key concept in LLM application development, progressing from basic model usage to memory-enabled chatbots.

## Project Structure

```
smart-ai-apps-playground/
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables (not committed)
├── shared/
│   ├── loader.py                  # Singleton model loader + CustomPrompt class
│   └── sample.py                  # Sample reviews + shared prompt templates
├── 01-model-comparison/
│   ├── README.md
│   └── cmp-models.py              # GPT-3.5 vs GPT-4 comparison
├── 02-json-output-parsing/
│   ├── README.md
│   └── json-prs-models.py         # Structured JSON output with Pydantic
├── 03-document-loading-splitting/
│   ├── README.md
│   └── doc-load-models.py         # PDF & web document loading + text splitting
├── 04-semantic-retrieval/
│   ├── README.md
│   └── retrieval-models.py        # Vector store + semantic retrieval
├── 05-chatbot-memory/
│   ├── README.md
│   ├── 1-manual-history.py        # Manual chat history
│   ├── 2-buffer-memory.py         # Buffer memory with RunnableWithMessageHistory
│   └── 3-summary-memory.py        # Rolling summary memory
└── 06-sequential-chain-vs-lcel/
    ├── README.md
    ├── 1-sequential-chain.py      # Legacy SequentialChain approach
    └── 2-lcel-pipeline.py         # Modern LCEL Runnable pipeline
```

## Exercises

### 01 — Model Comparison
Compares GPT-3.5-turbo and GPT-4 responses across 3 prompt types (creative writing, factual questions, instruction-following). Uses a `CustomPrompt` class with private properties and a singleton model loader to avoid reloading models.

### 02 — JSON Output Parsing
Demonstrates structured output extraction using a Pydantic `MovieInfo` schema and LangChain's `JsonOutputParser`. Builds a `prompt | llm | parser` chain that forces the model to return valid, typed JSON.

### 03 — Document Loading & Text Splitting
Loads content from a remote PDF and a web page using `PyPDFLoader` and `WebBaseLoader`. Splits documents with both `CharacterTextSplitter` and `RecursiveCharacterTextSplitter` and compares chunk statistics.

### 04 — Semantic Retrieval System
Embeds document chunks with `OpenAIEmbeddings` (`text-embedding-3-small`) into a Chroma vector store, then retrieves the most relevant passages for natural language queries using a `VectorStoreRetriever`.

### 05 — Chatbot with Memory (3 implementations)
| File | Strategy |
|---|---|
| `1-manual-history.py` | Manually manage `ChatMessageHistory` |
| `2-buffer-memory.py` | `RunnableWithMessageHistory` stores every message per session |
| `3-summary-memory.py` | LLM updates a rolling summary after each turn to save tokens |

### 06 — Sequential Chain vs LCEL Pipeline
Implements the same three-step product review analysis pipeline (sentiment → summary → response) using two different approaches side by side: the legacy `SequentialChain` from `langchain-classic` and the modern LCEL `RunnablePassthrough` pipeline.

## Shared Utilities

### `shared/loader.py`
- **`load_model(model_id, temperature, max_tokens)`** — Singleton factory; instantiates a `ChatOpenAI` once and reuses it on subsequent calls.
- **`load_gpt3()`** — Returns `gpt-3.5-turbo` at `temperature=0.8`.
- **`load_gpt4()`** — Returns `gpt-4` at `temperature=0.2`.
- **`CustomPrompt`** — Immutable data class with private fields (`prompt_type`, `prompt`, `behaviour`) exposed via read-only `@property` getters.

### `shared/sample.py`
- **`get_reviews()`** — Returns a list of `CustomReview` objects (positive, neutral, negative) used by exercise 06.
- **`DefaultPromptTemplate`** — Shared prompt strings for sentiment analysis, summarisation, and response generation.

## Setup

**Prerequisites:** Python 3.12+, OpenAI API key

1. Clone the repository and create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   USER_AGENT=smart-ai-apps-playground/1.0
   ```

4. Run any exercise:
   ```bash
   python 01-model-comparison/cmp-models.py
   python 02-json-output-parsing/json-prs-models.py
   python 03-document-loading-splitting/doc-load-models.py
   python 04-semantic-retrieval/retrieval-models.py
   python 05-chatbot-memory/1-manual-history.py
   python 05-chatbot-memory/2-buffer-memory.py
   python 05-chatbot-memory/3-summary-memory.py
   python 06-sequential-chain-vs-lcel/1-sequential-chain.py
   python 06-sequential-chain-vs-lcel/2-lcel-pipeline.py
   ```

## Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `langchain` | ≥1.2.13 | LLM application framework |
| `langchain-openai` | ≥1.1.12 | OpenAI model + embeddings integration |
| `langchain-core` | ≥1.2.22 | Runnables, prompts, parsers |
| `langchain-community` | ≥0.4.1 | Document loaders (`PyPDFLoader`, `WebBaseLoader`) |
| `langchain-text-splitters` | ≥1.1.1 | `CharacterTextSplitter`, `RecursiveCharacterTextSplitter` |
| `langchain-classic` | ≥1.0.3 | Legacy `LLMChain` and `SequentialChain` |
| `langchain-chroma` | ≥1.1.0 | Chroma vector store integration |
| `chromadb` | ≥1.5.5 | Local vector database |
| `openai` | ≥2.30.0 | OpenAI API client |
| `pydantic` | ≥2.12.5 | Structured output schemas |
| `python-dotenv` | ≥1.2.2 | Environment variable management |
| `beautifulsoup4` | ≥4.14.3 | HTML parsing for `WebBaseLoader` |
| `lxml` | ≥6.0.2 | XML/HTML parser backend |
| `pypdf` | ≥6.9.2 | PDF parsing for `PyPDFLoader` |

## License

This project is licensed under the [MIT License](LICENSE).
