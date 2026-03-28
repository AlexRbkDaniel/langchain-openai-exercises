from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt4

load_dotenv()

print("Loading models...")
llm: ChatOpenAI = load_gpt4()

# --- Simple Manual History ---
history = ChatMessageHistory()
history.add_message(SystemMessage(content="You are a helpful assistant."))
history.add_user_message("Hello, my name is Diana.")

ai_response = llm.invoke(history.messages)
history.add_ai_message(ai_response.content)

print("\nConversation History:")
for msg in history.messages:
    print(f"  {msg.type}: {msg.content}")

