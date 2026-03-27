from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt3, load_gpt4, CustomPrompt

load_dotenv()

print("Loading models...")
gpt3_llm: ChatOpenAI = load_gpt3()
gpt4_llm: ChatOpenAI = load_gpt4()

customPrompts = [
    CustomPrompt("Creative writing", "Write a short poem about artificial intelligence.",
                 "You are a supportive AI bot that behaves like a poet."),
    CustomPrompt("Factual questions", "What are the key components of a neural network?",
                 "You are a supportive AI bot that provides concise and accurate answers to factual questions."),
    CustomPrompt("Instruction-following", "List 5 tips for effective time management.",
                 "You are a supportive AI bot that provides step-by-step instructions for effective time management.")
]

print("\nTesting models...")
print("Comparing GPT-3.5 and GPT-4 responses to the same prompt...")

print("\nGPT-3.5 with temperature=0.8 and max_tokens=512:")
for prompt in customPrompts:
    gpt3_response = gpt3_llm.invoke(
        [
            SystemMessage(content=prompt.behaviour),
            HumanMessage(content=prompt.prompt)
        ]
    )
    print(f"Prompt: {prompt.prompt}")
    print(f"GPT-3.5 response: {gpt3_response.content}")

print("\nGPT-4 with temperature=0.2 and max_tokens=512:")
for prompt in customPrompts:
    gpt4_response = gpt4_llm.invoke(
        [
            SystemMessage(content=prompt.behaviour),
            HumanMessage(content=prompt.prompt)
        ]
    )
    print(f"Prompt: {prompt.prompt}")
    print(f"GPT-4 response: {gpt4_response.content}")
