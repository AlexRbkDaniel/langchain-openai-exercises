from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from shared.loader import load_gpt4


class MovieInfo(BaseModel):
    title: str = Field(description="Title of the movie")
    director: str = Field(description="Director of the movie")
    year: int = Field(description="Year the movie was released")
    genre: str = Field(description="Genre of the movie")


# Create your JSON parser
json_parser = JsonOutputParser(pydantic_object=MovieInfo)

# Create the format instructions
format_instructions = """RESPONSE FORMAT: Return ONLY a single JSON object—no markdown, no examples, no extra keys.  It must look exactly like:
{
  "title": "movie title",
  "director": "director name",
  "year": 2000,
  "genre": "movie genre"
}

IMPORTANT: Your response must be *only* that JSON.  Do NOT include any illustrative or example JSON."""

# Load llm model
print("Loading models...")
load_dotenv()
llm = load_gpt4()

# Create prompt template with instructions
prompt_template = PromptTemplate(
    template="""You are a JSON-only assistant.

Task: Generate info about the movie "{movie_name}" in JSON format.

{format_instructions}
""",
    input_variables=["movie_name"],
    partial_variables={"format_instructions": format_instructions},
)

# Create the chain
movie_chain = prompt_template | llm | json_parser

# Test with a movie name
movie_name = "The Matrix"
result =  movie_chain.invoke({"movie_name": movie_name})

# Print the structured result
print("Parsed result:")
print(f"Title: {result['title']}")
print(f"Director: {result['director']}")
print(f"Year: {result['year']}")
print(f"Genre: {result['genre']}")
