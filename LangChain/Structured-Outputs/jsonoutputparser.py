from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")

parser = JsonOutputParser()

temp = PromptTemplate(
    template='Give me name, age and city of fictional person \n  {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = temp.format()

# print('Prompt: ', prompt)

# result = model.invoke(prompt)

# ans = parser.parse(result.content)

chain = temp | model | parser

result = chain.invoke({})

print(result)
