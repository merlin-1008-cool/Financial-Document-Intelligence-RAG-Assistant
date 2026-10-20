Financial Document Intelligence RAG Assistant

Project Overview

The Financial Document Intelligence RAG Assistant is an AI-powered application that answers questions about financial documents using Retrieval-Augmented Generation (RAG).

The application retrieves relevant information from uploaded financial documents and uses a language model to generate answers grounded in the available information.

It is designed to help users find financial policy information through a simple, interactive interface.

Key Features

	•	PDF Document Processing: Extracts text from financial documents.
	•	Text Chunking: Divides extracted text into smaller chunks for efficient retrieval.
	•	Embedding Generation: Converts text into numerical vector representations.
	•	Vector Database: Uses ChromaDB to store and retrieve document embeddings.
	•	Semantic Search: Retrieves document passages relevant to a user’s question.
	•	AI-Powered Answers: Uses an Ollama-hosted language model to generate responses from retrieved context.
	•	Source Transparency: Displays retrieved passages, page numbers, and source information.
	•	Responsible Responses: Supports identifying questions that cannot be answered from the available documents.
	•	Interactive Interface: Provides a Streamlit-based question-and-answer experience.

Technologies Used

	•	Python
	•	Streamlit
	•	Retrieval-Augmented Generation (RAG)
	•	ChromaDB
	•	Text Embeddings
	•	Ollama
	•	Large Language Models (LLMs)
	•	PDF Text Extraction

How It Works

	1	Financial documents are loaded into the application.
	2	Text is extracted from the documents.
	3	The extracted text is divided into smaller chunks.
	4	Embeddings are generated for the chunks.
	5	The embeddings are stored in ChromaDB.
	6	A user submits a question through the Streamlit interface.
	7	The system retrieves relevant document passages.
	8	The language model generates an answer using the retrieved context.
	9	The application displays the answer and relevant source passages.

Project Structure

Financial-Document-Intelligence-RAG-Assistant/
│
├── app.py
├── src/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── embedding_generator.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   ├── test_document_pipeline.py
│   ├── test_embedding_generator.py
│   ├── test_rag_pipeline.py
│   ├── test_text_chunker.py
│   └── test_vector_store.py
│
└── test_document_loader.py

This structure lists the core files identified during development. Additional configuration, data, and documentation files may also be present.

Example Questions

Users can ask questions such as:

	•	What is the minimum age requirement for a personal loan?
	•	What is the minimum annual income required?
	•	What is the permitted personal loan amount range?
	•	What documents must an applicant provide?
	•	Does the policy specify a maximum age limit?

The answers depend on the information available in the loaded documents.

Responsible AI and Limitations

The assistant is designed to ground its responses in retrieved document content. However, retrieval and language-model generation can still produce incomplete or inaccurate answers.

Important considerations include:

	•	Answers depend on the quality and completeness of the source documents.
	•	Information absent from the documents cannot reliably be established by the assistant.
	•	Generated answers should be checked against the original documents for important financial decisions.
	•	The application does not replace professional financial advice or a bank’s formal loan approval process.

Potential Future Enhancements

	•	Support for additional document formats.
	•	Multiple-document management and source selection.
	•	Improved retrieval and answer-quality evaluation.
	•	Document citations linked directly to source passages.
	•	Enhanced interface and document management features.
	•	Deployment as a web application.

Disclaimer

The application is an educational and portfolio project. Any sample financial policies used for demonstration are fictional and should not be treated as official banking policies.