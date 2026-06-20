from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")

schema = [
    ResponseSchema(name='fact1', description='Fact 1 about topic'),
    ResponseSchema(name='fact2', description='Fact 2 about topic'),
    ResponseSchema(name='fact3', description='Fact 3 about topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

temp = PromptTemplate(
    template='Give 3 facts about {topic} \n  {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = temp.invoke({'topic': 'black hole'})

print('Prompt: ', prompt)

result = model.invoke(prompt)

ans = parser.parse(result.content)

print(ans)
