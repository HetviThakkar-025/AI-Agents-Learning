# OLD VERSION

# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

# from langchain_community.document_loaders import DirectoryLoader, TextLoader

# # Note: You must specify a loader_cls (like TextLoader) for it to read files
# loader = DirectoryLoader('./my_documents_folder', glob="*.txt", loader_cls=TextLoader)
# docs = loader.load()

# print(f"Loaded {len(docs)} documents.")

# LATEST STANDARD VERSION

from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document


def lazy_pdf_loader(file_path: Path):
    """Loads a single PDF page-by-page."""
    reader = PdfReader(file_path)
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        yield Document(
            page_content=text,
            metadata={"source": str(file_path), "page": page_num}
        )


def lazy_directory_loader(directory_path: str, glob_pattern: str = "*.pdf"):
    """Scans a directory and streams documents from all matching files."""
    path = Path(directory_path)

    # rglob searches the directory and all its subdirectories
    for file_path in path.rglob(glob_pattern):
        if file_path.is_file():
            print(f"Reading file: {file_path.name}")
            # Delegate loading to our single-file loader
            yield from lazy_pdf_loader(file_path)

# --- EXECUTION ---

# 1. Stream documents one-by-one to save memory
print("--- Streaming files line by line ---")
for doc in lazy_directory_loader("./my_documents_folder"):
    print(f"Loaded: {doc.metadata['source']} (Page {doc.metadata['page']})")

# 2. Or exhaust the generator into a list if you want to inspect or count them
print("\n--- Collecting all into a standard list ---")
all_docs = list(lazy_directory_loader("./my_documents_folder"))
print(f"Total pages loaded across all files: {len(all_docs)}")
