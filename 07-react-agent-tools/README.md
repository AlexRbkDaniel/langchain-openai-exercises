# 07 — ReAct Agent with Custom Tools

Build a LangChain **ReAct** (Reason + Act) agent that decides which tool to call based on a natural language question, executes it, observes the result, and repeats until it can give a final answer.

## What It Does

- Defines two custom `@tool`-decorated functions: a **calculator** and a **text formatter**
- Wires them into a ReAct agent via `create_react_agent` + `AgentExecutor`
- Runs 4 test questions and prints the agent's reasoning chain and final answer for each

## Files

| File | Purpose |
|---|---|
| `react-agent.py` | Full agent definition, tool implementations, and test runner |

## Key Concepts

- **`@tool`** — decorator that registers a plain Python function as a LangChain tool; the docstring becomes the description the agent reads to decide when to use it
- **ReAct loop** — the agent alternates between *Thought → Action → Observation* cycles until it reaches a *Final Answer*
- **`create_react_agent`** — builds the agent from an LLM, a list of tools, and a `PromptTemplate` that contains the ReAct scaffolding (`{tools}`, `{tool_names}`, `{agent_scratchpad}`)
- **`AgentExecutor`** — runs the loop, routes tool calls, injects observations back into the prompt, and enforces `handle_parsing_errors=True` so malformed LLM output doesn't crash the run
- **`eval()` sandbox** — `{"__builtins__": {}}` strips all Python built-ins from the eval context so only arithmetic operators work; dangerous calls like `__import__` raise a `NameError` instead

## Tools

### `calculator`
Evaluates a plain arithmetic expression string and returns the result.
```
Input:  "25 + 63"
Output: "88"
```

### `format_text`
Converts text to `uppercase`, `lowercase`, or `titlecase`.
```
Input:  "uppercase: hello world"
Output: "HELLO WORLD"
```

## ReAct Loop Flow

```
Question
    ↓
Thought: decide which tool is needed
    ↓
Action: <tool_name>
Action Input: <tool_input>
    ↓
Observation: <tool_output>
    ↓
Thought: is the answer ready?
    ├── No  → loop back to Action
    └── Yes → Final Answer
```

## Run

```bash
python 07-react-agent-tools/react-agent.py
```

## Sample Interactions

| Question | Tool Used | Final Answer |
|---|---|---|
| `What is 25 + 63?` | `calculator` | `88` |
| `Convert 'hello world' to uppercase` | `format_text` | `HELLO WORLD` |
| `Calculate 15 * 7` | `calculator` | `105` |
| `titlecase: langchain is awesome` | `format_text` | `Langchain Is Awesome` |

## Things to Try

- Add a third tool (e.g. a string reverser or a word counter) and test whether the agent picks it up automatically
- Set `max_iterations` on `AgentExecutor` to limit the ReAct loop depth
- Replace `load_gpt4()` with `load_gpt3()` and compare how reliably each model follows the ReAct format
- Add `return_intermediate_steps=True` to `AgentExecutor` to inspect every thought-action-observation step in the result dict
