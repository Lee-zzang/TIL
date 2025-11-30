# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 모델 초기화
# llm = ChatOpenAI(model="gpt-4o-mini")
llm = ChatOllama(model="deepseek-r1:14b")

messages = [
    SystemMessage("너는 사용자를 도와주는 상담사야."),
]

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    messages.append(HumanMessage(user_input))

    response = llm.stream(messages)

    ai_message = None
    for chunk in response:
        print(chunk.content, end="")
        if ai_message is None:
            ai_message = chunk
        else:
            ai_message += chunk
    print("")
    message_only = ai_message.content.split("</think>")[1].strip()
    messages.append(AIMessage(message_only))
