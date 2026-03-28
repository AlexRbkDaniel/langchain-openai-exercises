# Exercise 3 — Document Loading & Text Splitting

Load content from a remote PDF and a web page, split it into chunks with two different strategies, and compare the results.

## What It Does

- Loads a LangChain research paper (PDF) from a remote URL using `PyPDFLoader`
- Loads the LangChain documentation introduction page using `WebBaseLoader`
- Splits the PDF document with two different text splitters
- Prints chunk statistics (count, average size, min/max, metadata keys, example chunk)

## Key Concepts

- **`PyPDFLoader`** — fetches and parses a remote PDF, returning one `Document` per page with metadata (`source`, `page`)
- **`WebBaseLoader`** — scrapes a web page using `BeautifulSoup` and returns it as a `Document`
- **`CharacterTextSplitter`** — splits on a fixed separator (`\n`), prioritising chunk size of 300 characters with 30-character overlap
- **`RecursiveCharacterTextSplitter`** — tries multiple separators (`\n\n`, `\n`, ` `) recursively to produce more natural chunks of 500 characters with 50-character overlap
- **`USER_AGENT`** — set via `os.environ` before imports to avoid `WebBaseLoader` warnings

## Splitter Comparison

| | `CharacterTextSplitter` | `RecursiveCharacterTextSplitter` |
|---|---|---|
| Chunk size | 300 chars | 500 chars |
| Overlap | 30 chars | 50 chars |
| Split strategy | Single separator (`\n`) | Tries `\n\n` → `\n` → ` ` recursively |
| Best for | Structured text with clear line breaks | General prose and mixed content |

## Sources

| Type | URL |
|---|---|
| PDF | LangChain Architecture Paper (IBM Cloud S3) |
| Web | `https://python.langchain.com/v0.2/docs/introduction/` |

## Run

```bash
python 03-document-loading-splitting/doc-load-models.py
```

## Things to Try

- Adjust `chunk_size` and `chunk_overlap` and observe how statistics change
- Apply the splitters to the web document instead of the PDF
- Add a third splitter (e.g. `TokenTextSplitter`) for further comparison
