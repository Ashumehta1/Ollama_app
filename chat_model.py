from langchain_community.llms import Ollama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
llm=Ollama(model="llama3")
chat_history=[
    SystemMessage(content="You are a helpful assistant.")
]
while True:
    user_input=input("Human: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI : ",result)