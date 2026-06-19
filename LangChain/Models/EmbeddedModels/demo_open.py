from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
"Delhi is the capital of India",
"Kolkata is the capital of West Bengal",
"Paris is the capital of France"
]

# result = embeddings.embed_query("What is LangChain?")
result = embeddings.embed_documents(documents)
print(result)