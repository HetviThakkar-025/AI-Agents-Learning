from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description='Give sentiment of feedback')


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify sentiment of following feedback into positive or negative \n {text} \n  {format_instruction}',
    input_variables=['text'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifer_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write appropriate response to this positive feedback \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Write appropriate response to this negative feedback \n {text}',
    input_variables=['text']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifer_chain | branch_chain

result = chain.invoke({'text': 'this is terrible smartphone'})

print(result)

chain.get_graph().print_ascii()
