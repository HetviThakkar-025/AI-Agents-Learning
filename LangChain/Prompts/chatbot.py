from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")

chat_history = [
    SystemMessage(content='You are an experienced and highly skilled doctor')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print('Groq: ', result.content)

print(chat_history)
