from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt4

load_dotenv()

print("Loading models...")
llm: ChatOpenAI = load_gpt4()

# --- Buffer Memory with RunnableWithMessageHistory ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm

store: dict[str, ChatMessageHistory] = {}


def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


conversation = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


def chat_simulation(runnable, inputs: list[str], session_id: str):
    """Run a series of inputs through the conversation chain and display responses"""
    print("\n=== Beginning Chat Simulation ===")

    for i, user_input in enumerate(inputs):
        print(f"\n--- Turn {i + 1} ---")
        print(f"Human: {user_input}")

        response = runnable.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}},
        )

        print(f"AI: {response.content}")

    print("\n=== End of Chat Simulation ===")


test_inputs = [
    "My favorite color is blue.",
    "I enjoy hiking in the mountains.",
    "What activities would you recommend for me?",
    "What was my favorite color again?",
    "Can you remember both my name and my favorite color?"
]

chat_simulation(conversation, test_inputs, session_id="buffer_session")

print("\nFinal Memory Contents:")
for msg in get_session_history("buffer_session").messages:
    print(f"  {msg.type}: {msg.content}")

