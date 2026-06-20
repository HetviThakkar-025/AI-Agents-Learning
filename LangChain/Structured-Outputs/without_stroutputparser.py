from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")

# 1st prompt: detailed report
temp1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


# 2nd prompt: summary
temp2 = PromptTemplate(
    template='Write a 5 line summary on following text /n {text}',
    input_variables=['text']
)

prompt1 = temp1.invoke({'topic': 'Black hole'})

result = model.invoke(prompt1)

prompt2 = temp2.invoke({'text': result.content})

result2 = model.invoke(prompt2)

print(result2.content)
