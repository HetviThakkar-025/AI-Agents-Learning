from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableBranch, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarise following text {text}',
    input_variables=['text']
)

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_chain, branch_chain)

result = chain.invoke({'topic': 'Russia vs Ukraine'})

print(result)

chain.get_graph().print_ascii()
