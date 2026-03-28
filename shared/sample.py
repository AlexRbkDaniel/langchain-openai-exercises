from shared.loader import CustomReview, CustomPrompt

customPrompts = [
    CustomPrompt("Creative writing", "Write a short poem about artificial intelligence.",
                 "You are a supportive AI bot that behaves like a poet."),
    CustomPrompt("Factual questions", "What are the key components of a neural network?",
                 "You are a supportive AI bot that provides concise and accurate answers to factual questions."),
    CustomPrompt("Instruction-following", "List 5 tips for effective time management.",
                 "You are a supportive AI bot that provides step-by-step instructions for effective time management.")
]

def get_prompts():
    return customPrompts

reviews = [
    CustomReview("""I absolutely love this coffee maker! It brews quickly and the coffee tastes amazing. 
The built-in grinder saves me so much time in the morning, and the programmable timer means 
I wake up to fresh coffee every day. Worth every penny and highly recommended to any coffee enthusiast.""",
                 "positive"),
    CustomReview("""Disappointed with this laptop. It's constantly overheating after just 30 minutes of use, 
and the battery life is nowhere near the 8 hours advertised - I barely get 3 hours. 
The keyboard has already started sticking on several keys after just two weeks. Would not recommend to anyone.""",
                 "negative")
]

def get_reviews():
    return reviews

class DefaultPromptTemplate:
    sentiment_template = """Analyze the sentiment of the following product review as positive, negative, or neutral.
    Provide your analysis in the format: "SENTIMENT: [positive/negative/neutral]"

    Review: {review}

    Your analysis:
    """
    summary_template = """Summarize the following product review into 3-5 key bullet points.
    Each bullet point should be concise and capture an important aspect mentioned in the review.

    Review: {review}
    Sentiment: {sentiment}

    Key points:
    """
    response_template = """Write a helpful response to a customer based on their product review.
    If the sentiment is positive, thank them for their feedback. If negative, express understanding 
    and suggest a solution or next steps. Personalize based on the specific points they mentioned.

    Review: {review}
    Sentiment: {sentiment}
    Key points: {summary}

    Response to customer:
    """
