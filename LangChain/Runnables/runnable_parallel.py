from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence


load_dotenv()
model1 = ChatGroq(model="llama-3.1-8b-instant")
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1st prompt: detailed report
prompt1 = PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='generate a linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model1, parser),
    'post': RunnableSequence(prompt2, model2, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})

print(result)

parallel_chain.get_graph().print_ascii()
