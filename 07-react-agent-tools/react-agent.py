from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from shared.loader import load_gpt4


@tool
def calculator(expression: str) -> str:
    """A simple calculator that can add, subtract, multiply, or divide two numbers.
    Input should be a mathematical expression like '2 + 2' or '15 / 3'."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error calculating: {str(e)}"


@tool
def format_text(text: str) -> str:
    """Format text to uppercase, lowercase, or title case.
       Input should be in format: '[format_type]: [text]'
       where format_type is 'uppercase', 'lowercase', or 'titlecase'."""
    try:
        format_type, text_to_format = text.split(": ", 1)
        format_type = format_type.strip().lower()
        method_map = {
            "uppercase": "upper",
            "lowercase": "lower",
            "titlecase": "title",
        }
        if format_type not in method_map:
            return "Invalid format type. Use 'uppercase', 'lowercase', or 'titlecase'."
        return getattr(text_to_format, method_map[format_type])()
    except Exception as e:
        return f"Error formatting text: {str(e)}"


tools = [calculator, format_text]

prompt_template = """You are a helpful assistant who can use tools to help with simple tasks.
You have access to these tools:

{tools}

The available tools are: {tool_names}

To use a tool, please use the following format:
```
Thought: I need to figure out what to do
Action: tool_name
Action Input: the input to the tool
```

After you use a tool, the observation will be provided to you:
```
Observation: result of the tool
```

Then you should continue with the thought-action-observation cycle until you have enough information to respond to the user's request directly.
When you have the final answer, respond in this format:
```
Thought: I know the answer
Final Answer: the final answer to the original query
```

Remember, when using the Calculator tool, the input must be valid mathematical expressions.

Begin!

Question: {input}
{agent_scratchpad}
"""
prompt = PromptTemplate.from_template(prompt_template)

load_dotenv()
llm: ChatOpenAI = load_gpt4()

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

test_questions = [
    "What is 25 + 63?",
    "Can you convert 'hello world' to uppercase?",
    "Calculate 15 * 7",
    "titlecase: langchain is awesome",
]

for question in test_questions:
    print(f"\n===== Testing: {question} =====")
    try:
        response = agent_executor.invoke({"input": question})
        print(f"Response: {response['output']}")
    except Exception as e:
        print(f"Error occurred: {e}")
