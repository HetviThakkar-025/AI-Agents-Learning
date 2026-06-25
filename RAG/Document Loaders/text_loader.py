# from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template='Write summary for poem \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

# older version

# loader = TextLoader('cricket.txt', encoding='utf-8')

# docs = loader.load()

# print(docs)

# latest version

# 1. Read the file using native Python
file_path = "cricket.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 2. Wrap it into a LangChain standard Document object
docs = [Document(page_content=text, metadata={"source": file_path})]

print(type(docs))

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))
