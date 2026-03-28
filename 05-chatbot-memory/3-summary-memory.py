from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt4

load_dotenv()

print("Loading models...")
llm: ChatOpenAI = load_gpt4()

# --- Summary Memory ---
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant.\n\nConversation summary so far:\n{summary}"),
    ("human", "{input}"),
])

summary_text = ""


def chat_with_summary(user_input: str) -> str:
    global summary_text

    response = llm.invoke(
        summary_prompt.format_messages(summary=summary_text, input=user_input)
    )

    # Update the running summary after each turn
    update = llm.invoke([
        SystemMessage(content="Update the conversation summary by incorporating this new exchange. Be concise."),
        HumanMessage(content=f"Existing summary: {summary_text}\n\nNew exchange:\nHuman: {user_input}\nAI: {response.content}"),
    ])
    summary_text = update.content

    return response.content


test_inputs = [
    "My favorite color is blue.",
    "I enjoy hiking in the mountains.",
    "What activities would you recommend for me?",
    "What was my favorite color again?",
    "Can you remember both my name and my favorite color?"
]

print("\n=== Chat Simulation with Summary Memory ===")
for i, user_input in enumerate(test_inputs):
    print(f"\n--- Turn {i + 1} ---")
    print(f"Human: {user_input}")
    print(f"AI: {chat_with_summary(user_input)}")
print("\n=== End of Chat Simulation ===")

print("\nFinal Memory Contents (Summary):")
print(summary_text)

