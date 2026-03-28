from langchain_openai import ChatOpenAI

_model_instances: dict[str, ChatOpenAI] = {}

def load_model(model_id: str, temperature: float = 0.2, max_tokens: int = 512) -> ChatOpenAI:
    if model_id not in _model_instances:
        print(f"Loading model '{model_id}'...")
        _model_instances[model_id] = ChatOpenAI(
            model=model_id,
            temperature=temperature,
            max_tokens=max_tokens
        )
        print(f"Model '{model_id}' loaded.")
    else:
        print(f"Reusing already loaded model '{model_id}'.")
    return _model_instances[model_id]


def load_gpt3() -> ChatOpenAI:
    return load_model("gpt-3.5-turbo", temperature=0.8)


def load_gpt4() -> ChatOpenAI:
    return load_model("gpt-4")

class CustomPrompt:
    def __init__(self, prompt_type: str, prompt: str, behaviour: str):
        self.__prompt_type = prompt_type
        self.__prompt = prompt
        self.__behaviour = behaviour

    @property
    def prompt_type(self) -> str:
        return self.__prompt_type

    @property
    def prompt(self) -> str:
        return self.__prompt

    @property
    def behaviour(self) -> str:
        return self.__behaviour

class CustomReview:
    def __init__(self, review: str, type: str):
        self.__review = review
        self.__type = type

    @property
    def review(self) -> str:
        return self.__review

    @property
    def type(self) -> str:
        return self.__type