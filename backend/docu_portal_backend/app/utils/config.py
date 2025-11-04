import os
from langchain_ollama import OllamaEmbeddings

# Global settings
UPLOAD_FOLDER = "./uploads"
PERSIST_DIRECTORY = "./chroma_db"

# Embedding model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
