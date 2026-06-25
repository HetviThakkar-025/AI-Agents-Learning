# OLDER VERSION

# from langchain_community.document_loaders import WebBaseLoader
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

# prompt = PromptTemplate(
#     template='Answer the following question \n {question} from the following text - \n {text}',
#     input_variables=['question', 'text']
# )

# parser = StrOutputParser()

# url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
# loader = WebBaseLoader(url)

# docs = loader.load()


# chain = prompt | model | parser

# print(chain.invoke(
#     {'question': 'What is the prodcut that we are talking about?', 'text': docs[0].page_content}))

# LATEST VERSION

import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document


def native_web_loader(url: str) -> list[Document]:
    """Fetches a webpage and cleanly loads its text content into a LangChain Document."""
    # 1. Fetch the raw HTML content
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    # 2. Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Kill all script and style elements to clean the noise
    for script in soup(["script", "style"]):
        script.extract()

    # 3. Extract the clean, human-readable text
    clean_text = soup.get_text(separator="\n")

    # Break into lines and clear leading/trailing whitespace
    lines = (line.strip() for line in clean_text.splitlines())
    # Drop blank lines
    chunks = [line for line in lines if line]
    final_content = "\n".join(chunks)

    # 4. Wrap directly into a core LangChain Document
    # Extract the webpage title for metadata tracking
    title = soup.title.string if soup.title else "Webpage"

    return [Document(
        page_content=final_content,
        metadata={"source": url, "title": title}
    )]


# --- EXECUTION ---
docs = native_web_loader("https://python.langchain.com/docs/introduction/")

print(f"Total documents: {len(docs)}")
print("\n--- Document Metadata ---")
print(docs[0].metadata)

print("\n--- Snippet of Web Content ---")
print(docs[0].page_content[:300])
