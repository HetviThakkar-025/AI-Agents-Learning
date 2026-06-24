from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")


def counter(text):
    return len(text.split())

# passthrough = RunnableLambda(counter)
# print(passthrough.invoke("Hi helo"))


prompt = PromptTemplate(
    template='Genearte joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'count': RunnableLambda(lambda x: len(x.split()))
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = chain.invoke({'topic': 'AI'})

print(result)

parallel_chain.get_graph().print_ascii()
