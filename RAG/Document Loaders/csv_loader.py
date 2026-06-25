# OLDER VERSION

# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader(file_path='Social_Network_Ads.csv')

# docs = loader.load()

# print(len(docs))
# print(docs[1])

# LATEST VERSION

import csv
from langchain_core.documents import Document

def lazy_csv_loader(file_path: str, content_column: str = None):
    """
    Reads a CSV file row-by-row and yields LangChain Documents.
    If content_column is specified, only that column's text becomes the main content, 
    and the rest goes into metadata. Otherwise, the whole row is formatted.
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        # csv.DictReader automatically uses the first row as column headers (keys)
        reader = csv.DictReader(f)
        
        for row_num, row in enumerate(reader, start=1):
            if content_column and content_column in row:
                # Use a specific column's text as the primary content
                page_content = row[content_column]
                # Store the other columns as metadata attributes
                metadata = {k: v for k, v in row.items() if k != content_column}
            else:
                # If no specific column is targeted, stringify the entire row data
                page_content = ", ".join([f"{k}: {v}" for k, v in row.items()])
                metadata = row.copy()
            
            # Inject structural tracking details into metadata
            metadata["source"] = file_path
            metadata["row"] = row_num
            
            yield Document(page_content=page_content, metadata=metadata)

# --- EXECUTION ---

# 1. Option A: Convert the stream completely into a list (Matches legacy behavior)
docs = list(lazy_csv_loader("Social_Network_Ads.csv"))
print(f"Total rows loaded: {len(docs)}")
print("\n--- First Row Document Structure ---")
print(docs[0])

# 2. Option B: Target a specific text column (Great for RAG data columns like 'review_text' or 'comments')
# targeted_docs = list(lazy_csv_loader("your_data.csv", content_column="Description"))