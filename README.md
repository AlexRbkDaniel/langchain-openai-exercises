# Smart AI Apps Playground

An educational Python playground for learning to build AI applications using LangChain and OpenAI models. Each exercise demonstrates a key concept in LLM application development.

## Project Structure

```
smart-ai-apps-playground/
├── main.py                   # Project entry point
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
├── shared/
│   └── loader.py             # Shared model loading utilities
├── exercise1/
│   ├── README.md             # Exercise instructions
│   └── cmp-models.py         # Model comparison solution
└── exercise2/
    ├── README.md             # Exercise instructions
    └── json-prs-models.py    # JSON output parsing solution
```

## Exercises

### Exercise 1 — Model Comparison
Compares GPT-3.5-turbo and GPT-4 responses across different prompt types (creative writing, factual questions, instruction-following) with varying temperature settings.

### Exercise 2 — JSON Output Parsing
Demonstrates structured output extraction from LLMs using Pydantic models and LangChain's `JsonOutputParser`. Builds a chain that forces the model to return valid, typed JSON.

## Setup

**Prerequisites:** Python 3.12+, OpenAI API key

1. Create and activate a virtual environment:
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
   ```

4. Run an exercise:
   ```bash
   python exercise1/cmp-models.py
   python exercise2/json-prs-models.py
   ```

## Tech Stack

| Library | Purpose |
|---------|---------|
| `langchain` | LLM application framework |
| `langchain-openai` | OpenAI model integration |
| `openai` | OpenAI API client |
| `pydantic` | Structured output schemas |
| `python-dotenv` | Environment variable management |
