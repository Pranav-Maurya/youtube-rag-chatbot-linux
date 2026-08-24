# AI-Powered YouTube Question Answering using RAG

A simple Retrieval-Augmented Generation (RAG) chatbot that retrieves a YouTube video's transcript, splits it into chunks, creates embeddings, stores them in ChromaDB, retrieves relevant context, and generates answers using Cohere.

## Project Highlights

- YouTube transcript retrieval
- Text chunking with LangChain
- Cohere embeddings
- ChromaDB vector database
- Retrieval-Augmented Generation
- Cohere LLM for answer generation
- Runs locally on Parrot OS Linux
- Developed and demonstrated inside a VirtualBox virtual machine

## Architecture

```text
User
  |
  v
YouTube URL
  |
  v
YouTube Transcript API
  |
  v
Text Chunking
  |
  v
Cohere Embeddings
  |
  v
ChromaDB
  |
  v
Retriever
  |
  v
Prompt + Context
  |
  v
Cohere LLM
  |
  v
Answer
```

## Technologies

| Technology | Purpose |
|---|---|
| Parrot OS | Linux environment |
| VirtualBox | Virtualization |
| Python | Application logic |
| Jupyter Notebook | Interactive development |
| YouTube Transcript API | Transcript retrieval |
| LangChain | RAG pipeline |
| Cohere | Embeddings and LLM |
| ChromaDB | Vector database |

## Requirements

- Parrot OS or another Debian-based Linux distribution
- Python 3
- Internet connection
- Cohere API key
- Jupyter Notebook

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YTRAG_Project
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` and add your Cohere API key:

```text
COHERE_API_KEY=your_new_api_key_here
```

Do not commit `.env`.

### 5. Start Jupyter

```bash
jupyter notebook
```

Open:

```text
YtRag_Linux_Final.ipynb
```

Run the cells in order.

## Usage

When prompted:

```text
Enter YouTube URL:
```

Paste a YouTube URL, for example:

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

After the transcript is processed, ask a question in the question cell.

Example:

```text
What is this video about?
```

## Linux and Cloud Computing Relevance

The project is executed inside a Parrot OS Linux virtual machine running on VirtualBox.

```text
Physical Computer
       |
Windows Host
       |
VirtualBox Hypervisor
       |
Parrot OS Linux VM
       |
Python + Jupyter
       |
RAG Chatbot
```

The project demonstrates Linux administration, virtual machines, virtualization, client/application execution, and a cloud-ready architecture. It does not claim to be deployed on AWS/Azure/GCP.

Virtualization is a foundational technology used by modern cloud infrastructure.

## Project Structure

```text
YTRAG_Project/
├── YtRag_Linux_Final.ipynb
├── requirements.txt
├── .env.example
├── .gitignore
├── run.sh
└── README.md
```

## Security

Never upload API keys to GitHub.

If an API key has previously been placed in a notebook or committed to Git, revoke it in the provider dashboard and create a new key.

## Future Scope

- Web interface
- Voice-based questions
- Multilingual support
- Support for PDFs and other documents
- Local LLM support
- Deployment on a cloud virtual machine

## Author

Pranav Mauraya
B.Tech Computer Science & Engineering
