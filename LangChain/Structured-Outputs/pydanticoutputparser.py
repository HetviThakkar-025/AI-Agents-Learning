from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")


class Person(BaseModel):
    name: str = Field(description='Name of person')
    age: int = Field(gt=18, description='Age of person')
    city: str = Field(gt=18, description='City of person')


parser = PydanticOutputParser(pydantic_object=Person)

temp = PromptTemplate(
    template='Generate name,age and city of fictional {place} person \n  {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = temp.invoke({'place': 'India'})

result = model.invoke(prompt)

ans = parser.parse(result.content)

print(ans)
