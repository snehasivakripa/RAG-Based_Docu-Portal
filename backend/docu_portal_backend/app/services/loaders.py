from langchain_community.document_loaders import WebBaseLoader, CSVLoader, PyPDFLoader

def load_website(urls):
    loader = WebBaseLoader(urls)
    return loader.load()

def load_csv(file_paths):
    docs = []
    for file_path in file_paths:
        loader = CSVLoader(file_path=file_path)
        docs.extend(loader.load())
    return docs

def load_pdf(pdf_files):
    docs = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(file_path=pdf_file)
        docs.extend(loader.load())
    return docs
