from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template='Genearte joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain joke - {text}',
    input_variables=['text']
)

parser = StrOutputParser()

# chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)
chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'cricket'})

print(result)

chain.get_graph().print_ascii()
