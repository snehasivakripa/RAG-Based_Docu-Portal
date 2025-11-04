from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from app.utils.config import embeddings, PERSIST_DIRECTORY

def split_documents(documents, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def store_documents(documents):
    splitted_docs = split_documents(documents)
    vectorstore = Chroma.from_documents(
        documents=splitted_docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )
    return vectorstore

def get_vectorstore():
    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )
