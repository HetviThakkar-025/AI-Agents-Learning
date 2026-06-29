from langchain_text_splitters import CharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader
from langchain_docling.loader import DoclingLoader
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import PipelineOptions

pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False

loader = DoclingLoader(
    file_path="../dl-curriculum.pdf",
    pipeline_options=pipeline_options
)

# TEXT

# text = """Space exploration has led to incredible scientific discoveries. From landing on the Moon
# to exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.

# These missions have not only expanded our knowledge of the
# universe but have also contributed to advancements in
# technology here on Earth. Satellite communications, GPS, and
# even certain medical imaging techniques trace their roots back
# to innovations driven by space programs."""

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=80,
#     chunk_overlap=0
# )

# result = splitter.split_text(text=text)

# PDF

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_documents(documents=docs)

print(result)
