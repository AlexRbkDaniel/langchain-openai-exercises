# 06 — Sequential Chain vs LCEL Pipeline

Compare two approaches to building multi-step LLM pipelines in LangChain: the legacy `SequentialChain` from `langchain-classic` and the modern **LCEL** (LangChain Expression Language) using `RunnablePassthrough`.

Both scripts run the same three-step review analysis pipeline and produce identical output, making it easy to compare readability, flexibility, and composability.

## What It Does

1. Loads a set of sample product reviews from `shared/sample.py`
2. Runs each review through a **three-step pipeline**:
   - **Sentiment analysis** — classifies the review as positive, neutral, or negative
   - **Summarisation** — produces a one-sentence summary of the review
   - **Response generation** — drafts a customer-service reply based on the review, sentiment, and summary
3. Prints the sentiment, summary, and generated response for each review

## Files

| File | Approach | Key Components |
|---|---|---|
| `1-sequential-chain.py` | Legacy `SequentialChain` | `LLMChain`, `SequentialChain` from `langchain-classic` |
| `2-lcel-pipeline.py` | Modern LCEL | `RunnablePassthrough.assign`, `RunnableLambda`, `StrOutputParser` |

## Key Concepts

- **`SequentialChain`** — chains multiple `LLMChain` steps together; each step's `output_key` becomes available as an `input_variable` for subsequent steps. Explicit and verbose.
- **LCEL (`|` operator)** — composes `PromptTemplate | ChatOpenAI | StrOutputParser` into a single `Runnable`. `RunnablePassthrough.assign()` threads intermediate results through the pipeline as dict keys.
- **`RunnableLambda`** — wraps a plain Python function so it satisfies the `Runnable[Any, Any]` interface expected by `RunnablePassthrough.assign()`.

## Pipeline Flow

```
Input: {"review": "..."}
       │
       ▼
RunnablePassthrough.assign(sentiment=...)   ← sentiment_chain
       │  adds "sentiment" key to dict
       ▼
RunnablePassthrough.assign(summary=...)     ← summary_chain (uses review + sentiment)
       │  adds "summary" key to dict
       ▼
RunnablePassthrough.assign(response=...)    ← response_chain (uses review + sentiment + summary)
       │
       ▼
Result: {"review": "...", "sentiment": "...", "summary": "...", "response": "..."}
```

## Run

```bash
python 06-sequential-chain-vs-lcel/1-sequential-chain.py
python 06-sequential-chain-vs-lcel/2-lcel-pipeline.py
```

## Approach Comparison

| | `SequentialChain` | LCEL Pipeline |
|---|---|---|
| Declaration style | Explicit chain list + variable names | Composable `\|` operator |
| Intermediate results | Passed automatically via `output_key` | Threaded as dict keys via `.assign()` |
| Debugging | `verbose=True` logs each step | Add `.with_config({"run_name": "..."})` per step |
| Flexibility | Fixed linear flow | Branching, parallel steps, streaming |
| Status | Legacy (`langchain-classic`) | Recommended for all new projects |

## Things to Try

- Add a fourth step (e.g. a translation chain) and observe how each approach handles the extension
- Enable `verbose=True` on the `SequentialChain` to inspect intermediate outputs
- Replace `load_gpt4()` with `load_gpt3()` and compare speed vs. quality
- Stream the LCEL pipeline output with `.stream()` instead of `.invoke()`
