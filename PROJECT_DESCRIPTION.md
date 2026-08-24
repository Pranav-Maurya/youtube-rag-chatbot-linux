# Project Description

This project implements a YouTube question-answering chatbot using Retrieval-Augmented Generation (RAG). A YouTube transcript is retrieved, divided into smaller chunks, converted into embeddings using Cohere, and stored in ChromaDB. When a user asks a question, the retriever selects relevant transcript chunks and the Cohere language model generates an answer using that context.

The application is developed and executed on Parrot OS Linux inside a VirtualBox virtual machine. This demonstrates Linux-based application execution and virtualization concepts relevant to cloud computing.
