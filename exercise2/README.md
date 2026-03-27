# Exercise 2 — JSON Output Parsing

Extract structured, typed data from an LLM using a Pydantic schema and LangChain's `JsonOutputParser`.

## What It Does

- Defines a `MovieInfo` Pydantic model with 4 typed fields: `title`, `director`, `year`, `genre`
- Builds a `prompt | llm | parser` chain that instructs GPT-4 to return **only** a valid JSON object
- Invokes the chain with a movie name and accesses the parsed fields directly as a Python dict

## Key Concepts

- **`JsonOutputParser`** — parses the LLM's raw string output into a Python dict, validated against the Pydantic schema
- **`PromptTemplate`** — injects `format_instructions` as a partial variable so the model always knows the expected output shape
- **LCEL chain (`|`)** — connects `PromptTemplate → ChatOpenAI → JsonOutputParser` in a single pipeline
- **Strict instructions** — the prompt explicitly forbids markdown, examples, and extra keys to ensure clean JSON output

## Pydantic Schema

```python
class MovieInfo(BaseModel):
    title: str      # Title of the movie
    director: str   # Director of the movie
    year: int       # Release year
    genre: str      # Genre
```

## Run

```bash
python exercise2/json-prs-models.py
```

## Expected Output

```
Parsed result:
Title: The Matrix
Director: The Wachowskis
Year: 1999
Genre: Science Fiction
```

## Things to Try

- Change `movie_name` to a different film and verify the parser handles it correctly
- Add more fields to `MovieInfo` (e.g. `rating`, `cast`) and update the format instructions
- Test with an obscure or fictional movie to see how the model handles uncertainty
