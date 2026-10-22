💰 Financial Document Intelligence RAG Assistant

An AI-Powered Financial Document Question-Answering System

🚀 Live Application

Try the application here:

👉 ⁠Open Financial Document Intelligence RAG Assistant

Ask questions about financial policy documents and receive AI-generated answers grounded in the relevant document passages.

📌 Project Overview

The Financial Document Intelligence RAG Assistant is an AI-powered application that enables users to retrieve information from financial documents using natural-language questions.

Traditional document analysis often requires users to search through lengthy PDFs manually. This project addresses that challenge by combining semantic search, vector databases, and Large Language Models (LLMs) in a Retrieval-Augmented Generation (RAG) pipeline.

The application extracts text from PDF documents, divides it into manageable chunks, generates vector embeddings, and stores them in ChromaDB. When a user submits a question, the system retrieves relevant passages and uses Groq to generate an answer based on the retrieved context.

The system is designed to reduce unsupported answers by instructing the language model to rely on the supplied document context and acknowledge when the available information is insufficient.

🎯 Project Objectives

* Automate information retrieval from financial policy documents.
* Enable natural-language question answering over document content.
* Implement a complete Retrieval-Augmented Generation workflow.
* Combine semantic search with Large Language Model inference.
* Provide a simple, accessible web interface using Streamlit.
* Deploy the application to Streamlit Community Cloud.

✨ Key Features

📄 PDF Text Extraction

Extracts textual content from PDF documents for downstream processing.

✂️ Intelligent Text Chunking

Splits extracted text into smaller, overlapping chunks to support effective semantic retrieval.

🧠 Semantic Embeddings

Uses the all-MiniLM-L6-v2 Sentence Transformer model to convert text into 384-dimensional vector embeddings.

🗄️ Vector Database

Uses ChromaDB to store document chunks and perform similarity-based retrieval.

🔎 Context-Aware Retrieval

Retrieves relevant document passages based on the semantic similarity between the user’s question and the stored document content.

🤖 AI-Powered Answer Generation

Uses the Groq API with the openai/gpt-oss-120b model to generate answers using the retrieved document context.

🛡️ Grounded Responses

Instructs the language model not to invent financial policies and to acknowledge when the provided documents do not contain sufficient information.

🌐 Cloud Deployment

Deployed using Streamlit Community Cloud, allowing users to access the application through a web browser without installing the project locally.

🏗️ System Architecture

The application follows a Retrieval-Augmented Generation architecture.



             Financial PDF Document
                       |
                       v
                PDF Text Extraction
                       |
                       v
                 Text Chunking
                       |
                       v
              Embedding Generation
            (all-MiniLM-L6-v2)
                       |
                       v
                  ChromaDB
              Vector Database
                       |
                       |
User Question --------+
       |
       v
Question Embedding
       |
       v
Semantic Similarity Search
       |
       v
Relevant Document Passages
       |
       v
Groq API (LLM Inference)
       |
       v
Context-Grounded Answer
       |
       v
Streamlit Web Interface


🛠️ Technology Stack:

Technology                                          Purpose

Python                                        Core programming language

Streamlit                                     Interactive web application

PyPDF                                         PDF text extraction

Sentence Transformers                         Text embedding generation

all-MiniLM-L6-v2                              Sentence embedding model

ChromaDB                                      Vector storage and similarity search

Groq API                                      Large Language Model inference

openai/gpt-oss-120b                           Answer generation

Git and GitHub                                Version control and source code management

Streamlit Community Cloud.                    Application deployment



📂 Project Structure:

Financial-Document-Intelligence-RAG-Assistant/
│
├── app.py
│
├── src/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── embedding_generator.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
├── data/
│   └── sample_documents/
│       └── sample_loan_policy.pdf
│
├── test_document_pipeline.py
├── test_embedding_generator.py
├── test_vector_store.py
├── test_rag_pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md

Note: The structure above represents the main application components and project files. Generated vector database files are excluded from version control.




💡 Example Questions:

The application uses a sample personal loan policy document for demonstration.

Users can ask questions such as:



         Question                                                     Expected Information

What is the minimum age required for a personal loan?                       21 years

What is the minimum annual income required?                                 ₹300,000

What documents are required to apply for a personal loan?       Identity proof, address proof, income proof, and recent bank statements

What is the minimum loan amount?                                             ₹50,000

What is the maximum loan amount?                                             ₹1,000,000


The answers depend on the content of the indexed document.


⚙️ Installation and Setup

Follow these steps to run the project locally.

Prerequisites

* Python 3.12
* Git
* A Groq API key

1. Clone the Repository:

   git clone https://github.com/merlin-1008-cool/Financial-Document-Intelligence-RAG-Assistant.git

   Navigate to the project directory:

   cd Financial-Document-Intelligence-RAG-Assistant

2. Create a Virtual Environment

   python3.12 -m venv .venv

3. Install Dependencies

   pip install -r requirements.txt

4. Configure the Groq API Key

   Obtain an API key from the ⁠Groq Console.
   For local development, set the environment variable in your terminal:

   export GROQ_API_KEY="your_actual_groq_api_key"

   Replace the placeholder with your actual key.


5. Run the Application

   streamlit run app.py

Streamlit will provide a local URL that you can open in your browser.


☁️ Deployment

The application is deployed on Streamlit Community Cloud.

The deployed version uses Streamlit Secrets to securely configure the Groq API key.

To configure the secret for your own deployment, use the following format in the Streamlit app’s Secrets settings:

GROQ_API_KEY = "your_actual_groq_api_key"

Do not commit this secret to your repository.

Live application: ⁠Financial Document Intelligence RAG Assistant


🧪 Testing and Validation

The project includes tests for its principal components:

* Document extraction and text processing.
* Embedding generation.
* Vector database operations.
* End-to-end retrieval and answer generation.

The application has been tested against the sample loan policy document. Example questions about the minimum income requirement and minimum age have returned the expected information.


🔒 Limitations and Future Improvements

Current Limitations

* Answers depend on the quality and completeness of the indexed documents.
* The current demonstration uses a sample personal loan policy PDF.
* AI-generated answers may occasionally be incomplete or inaccurate.
* Financial decisions should not be made solely on the basis of AI-generated responses.

Potential Future Improvements

* Support for multiple financial documents.
* Document upload and indexing through the user interface.
* Improved source citations and passage highlighting.
* Support for additional document formats.
* Enhanced retrieval evaluation and automated testing.
* Authentication and access controls for sensitive documents.

🎓 Skills Demonstrated

This project demonstrates practical experience with:

* Python application development.
* Document processing and text preprocessing.
* Natural Language Processing (NLP).
* Semantic embeddings and vector similarity search.
* Vector databases and information retrieval.
* Retrieval-Augmented Generation (RAG).
* Large Language Model API integration.
* Prompt engineering and context-grounded responses.
* Streamlit application development.
* Cloud deployment and environment configuration.
* Git and GitHub version control.


👨‍💻 Author

Merlin Martina I

AI and Data Science Portfolio Project

⁠GitHub Profile

⸻

⭐ Support

If you find this project useful, consider giving the repository a star on GitHub.

Built to demonstrate the practical application of RAG, semantic search, and LLMs for financial document intelligence.



