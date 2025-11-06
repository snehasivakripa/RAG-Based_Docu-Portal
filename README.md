# 🧠 RAG-Based Docu Portal

RAG-Based Docu Portal is an AI-powered web application that allows users to upload documents and ask natural-language questions about them. It leverages **Retrieval-Augmented Generation (RAG)** to provide answers grounded in your documents.

---

## 🚀 Features

- 📄 Upload PDFs or provide URLs to ingest documents  
- 💬 Ask natural-language questions about uploaded content  
- 🤖 AI-powered responses grounded in your documents (RAG)  
- 🔍 Supports multiple document types: PDF, CSV, and web pages  

---

## 🧠 How It Works (RAG Flow)

1. **Document Upload** – Users upload PDFs, CSVs, or provide web URLs.  
2. **Document Parsing & Chunking** – Text is extracted and split into chunks.  
3. **Embedding Generation** – Chunks are converted into vector embeddings using **OllamaEmbeddings**.  
4. **Vector Storage** – Chunks are stored in **ChromaDB** for retrieval.  
5. **Querying / RAG** – User questions retrieve relevant chunks and generate answers grounded in those documents.  

---

## 🛠️ Tech Stack

### Frontend
- Angular 16+  
- TypeScript  
- Angular Material  
- RxJS  
- HTML5 / SCSS  

### Backend
- Python 3.11+  
- Flask – REST API server  
- Flask-CORS – Enable cross-origin requests  
- LangChain – RAG pipeline & document handling  
- Chroma – Vector database for embeddings  
- OllamaEmbeddings – Generate embeddings from documents  
- PyPDFLoader / CSVLoader / WebBaseLoader – Load PDFs, CSVs, and web pages  
- dotenv – Environment variable management  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/snehasivakripa/RAG-Based_Docu-Portal.git
cd RAG-Based_Docu-Portal

