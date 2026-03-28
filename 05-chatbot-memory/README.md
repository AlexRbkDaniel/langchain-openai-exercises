# Exercise 5 — Chatbot with Memory

Implements three different conversation memory strategies using LangChain, each in its own standalone script.

## Files

| File | Memory Strategy | Token Usage |
|---|---|---|
| `1-manual-history.py` | Manual `ChatMessageHistory` | Grows linearly |
| `2-buffer-memory.py` | `RunnableWithMessageHistory` (full buffer) | Grows linearly |
| `3-summary-memory.py` | LLM-generated rolling summary | Stays small |
| `chatbot-memory-models.py` | Combined reference (all 3 in one file) | — |

---

## Implementation 1 — Manual History (`1-manual-history.py`)

The simplest approach: a `ChatMessageHistory` object where you manually call `add_user_message()`, invoke the LLM, then call `add_ai_message()` yourself.

**Best for:** understanding how message history works under the hood.

```bash
python 05-chatbot-memory/1-manual-history.py
```

---

## Implementation 2 — Buffer Memory (`2-buffer-memory.py`)

Uses `RunnableWithMessageHistory` to wrap a `ChatPromptTemplate | ChatOpenAI` chain. History is **automatically** appended per `session_id` — no manual message management needed.

**Best for:** multi-turn conversations where full context must be preserved.

```bash
python 05-chatbot-memory/2-buffer-memory.py
```

### How It Works

```
User input
    ↓
RunnableWithMessageHistory
    ├── Injects full history into prompt via MessagesPlaceholder
    ├── Calls ChatOpenAI
    └── Appends HumanMessage + AIMessage to session store
```

---

## Implementation 3 — Summary Memory (`3-summary-memory.py`)

After each turn the LLM is asked to update a `summary_text` string that captures the conversation so far. Only the summary is injected into the next prompt — not the raw message history.

**Best for:** long conversations where keeping every message would exceed the context window.

```bash
python 05-chatbot-memory/3-summary-memory.py
```

### How It Works

```
User input + current summary
    ↓ llm.invoke()
AI response
    ↓ llm.invoke() — "update the summary"
Updated summary_text  ← used in next turn
```

---

## Memory Strategy Comparison

| | Manual History | Buffer Memory | Summary Memory |
|---|---|---|---|
| Stores | All messages | All messages | Summary string only |
| Token growth | Linear | Linear | Constant |
| Exact recall | ✅ | ✅ | ❌ (paraphrased) |
| Multi-session | ❌ | ✅ (by `session_id`) | ❌ |
| API calls/turn | 1 | 1 | 2 (response + summary update) |

## Key Concepts

- **`ChatMessageHistory`** — in-memory list of `BaseMessage` objects
- **`RunnableWithMessageHistory`** — LangChain runnable that auto-manages history; requires `input_messages_key` and `history_messages_key`
- **`MessagesPlaceholder`** — injects the full message list into a `ChatPromptTemplate` at the correct position
- **`session_id`** — key used to look up or create an isolated history store per conversation
