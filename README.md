# youtube-rag-chatbot-linux

AI-powered YouTube question answering chatbot using RAG, LangChain, Cohere, and ChromaDB, developed on Parrot OS Linux.

## Features

- Ingests a YouTube video's transcript
- Splits transcript into chunks for retrieval
- Stores embeddings in local ChromaDB
- Answers questions with Cohere using a RAG pipeline

## Prerequisites (Parrot OS Linux)

- Python 3.10+
- `python3-venv` package
- A Cohere API key

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Export your Cohere API key:

```bash
export COHERE_API_KEY="your_api_key_here"
```

## Usage

```bash
python chatbot.py --video "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Then enter questions in the prompt. Type `exit` or `quit` to stop.

## Test

```bash
python -m unittest -q
```
