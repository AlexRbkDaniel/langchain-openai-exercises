from dotenv import load_dotenv
from langchain_classic.chains.llm import LLMChain
from langchain_classic.chains.sequential import SequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt4, CustomReview
from shared.sample import get_reviews, DefaultPromptTemplate

load_dotenv()
llm: ChatOpenAI = load_gpt4()

reviews = get_reviews()

sentiment_prompt_template = PromptTemplate(template=DefaultPromptTemplate.sentiment_template,
                                           input_variables=["review"])
sentiment_chain = LLMChain(llm=llm, prompt=sentiment_prompt_template, output_key="sentiment")

summary_prompt_template = PromptTemplate(template=DefaultPromptTemplate.summary_template,
                                         input_variables=["review", "sentiment"])
summary_chain = LLMChain(llm=llm, prompt=summary_prompt_template, output_key="summary")

response_prompt_template = PromptTemplate(template=DefaultPromptTemplate.response_template,
                                          input_variables=["review", "sentiment", "summary"])
response_chain = LLMChain(llm=llm, prompt=response_prompt_template, output_key="response")

overall_chain = SequentialChain(
    chains=[sentiment_chain, summary_chain, response_chain],
    input_variables=["review"],
    output_variables=["sentiment", "summary", "response"],
    verbose=True
)


def test_chain(review: CustomReview) -> None:
    """Test both chain implementations with the given review"""
    print("\n" + "=" * 50)
    print(f"Review: {review.review}")
    print(f"Sentiment: {review.type}")
    print("\n Traditional Chain Result:")
    result = overall_chain.invoke(review.review)
    print(f"Sentiment: {result['sentiment']}")
    print(f"Summary: {result['summary']}")
    print(f"Response: {result['response']}")


for review in reviews:
    test_chain(review)
