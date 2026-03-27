# Exercise 1 — Model Comparison

Compare responses from **GPT-3.5-turbo** and **GPT-4** across different prompt types and temperature settings.

## What It Does

- Loads both models via the shared singleton `loader.py` (models are instantiated once and reused)
- Defines 3 prompts using the `CustomPrompt` class, each with a `prompt_type`, `prompt`, and `behaviour` (system message)
- Sends the same prompts to both models and prints their responses side by side

## Key Concepts

- **Singleton pattern** — `load_gpt3()` / `load_gpt4()` return a cached instance; subsequent calls skip re-instantiation
- **`CustomPrompt` class** — immutable data holder with private fields (`__prompt_type`, `__prompt`, `__behaviour`) exposed via read-only `@property` getters, no setters
- **Temperature** — GPT-3.5 runs at `temperature=0.8` (more creative), GPT-4 at `temperature=0.2` (more deterministic)
- **`SystemMessage` + `HumanMessage`** — each invocation passes a behaviour instruction alongside the user prompt

## Prompt Types Tested

| Type | Prompt | System Behaviour |
|---|---|---|
| Creative writing | Write a short poem about artificial intelligence | Behave like a poet |
| Factual questions | What are the key components of a neural network? | Provide concise, accurate answers |
| Instruction-following | List 5 tips for effective time management | Provide step-by-step instructions |

## Run

```bash
python exercise1/cmp-models.py
```

## Observations to Note

- How does **temperature** affect creativity vs. consistency?
- Where does GPT-4 produce noticeably better output than GPT-3.5?
- Does the system `behaviour` message meaningfully change the tone of the response?
