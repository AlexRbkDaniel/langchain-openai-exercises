from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt4, CustomReview
from shared.sample import get_reviews, DefaultPromptTemplate

load_dotenv()
llm: ChatOpenAI = load_gpt4()

reviews = get_reviews()

sentiment_chain = (
        PromptTemplate.from_template(DefaultPromptTemplate.sentiment_template)
        | llm
        | StrOutputParser()
)

summary_chain = (
    PromptTemplate.from_template(DefaultPromptTemplate.summary_template)
    | llm
    | StrOutputParser()
)

response_chain = (
    PromptTemplate.from_template(DefaultPromptTemplate.response_template)
    | llm
    | StrOutputParser()
)

overall_chain = (
    RunnablePassthrough.assign(sentiment=RunnableLambda(lambda x: sentiment_chain.invoke({"review": x["review"]})))
    | RunnablePassthrough.assign(summary=RunnableLambda(lambda x: summary_chain.invoke({"review": x["review"], "sentiment": x["sentiment"]})))
    | RunnablePassthrough.assign(response=RunnableLambda(lambda x: response_chain.invoke({"review": x["review"], "sentiment": x["sentiment"], "summary": x["summary"]})))
)

def test_chain(review: CustomReview) -> None:
    print("\n" + "=" * 50)
    print(f"Review: {review.review}")
    print(f"Sentiment: {review.type}")
    print("\n LCEL Result:")
    result = overall_chain.invoke({"review": review.review})
    print(f"Sentiment: {result['sentiment']}")
    print(f"Summary: {result['summary']}")
    print(f"Response: {result['response']}")


for review in reviews:
    test_chain(review)
