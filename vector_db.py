from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

def load_documents():
    raw_docs = TextLoader("./docs/dataset.txt").load()
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    return text_splitter.split_documents(raw_docs)