# for pdfs having images, tables etc -> Docling
# from langchain_docling.loader import DoclingLoader
from langchain_core.documents import Document
from pypdf import PdfReader


# the cutting-edge standard is IBM's Docling, which LangChain heavily integrates with for high-fidelity text, layout, and table parsing.
# loader = DoclingLoader(file_path="dl-curriculum.pdf")
# docs = loader.load()
# print(docs.metadata)

# load raw bytes using native Python/lightweight libraries and wrap them into standard core Document primitives natively using lazy_load generators.
def lazy_pdf_loader(file_path: str):
    reader = PdfReader(file_path)
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        # Creating standard LangChain core Documents directly
        yield Document(
            page_content=text,
            metadata={"source": file_path, "page": page_num}
        )


# Execution streaming chunk by chunk (memory-efficient)
# for doc in lazy_pdf_loader("dl-curriculum.pdf"):
#     print(doc.metadata)

docs = list(lazy_pdf_loader("dl-curriculum.pdf"))

print(f"Total pages loaded: {len(docs)}")

print("\n--- First Document Object ---")
print(docs[0])
