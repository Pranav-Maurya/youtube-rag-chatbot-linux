import argparse
import os
from typing import Optional
from urllib.parse import parse_qs, urlparse


def extract_video_id(url_or_id: str) -> str:
    value = url_or_id.strip()
    if len(value) == 11 and "://" not in value and "/" not in value:
        return value

    parsed = urlparse(value)
    host = parsed.netloc.lower()

    if host in {"youtu.be", "www.youtu.be"}:
        return parsed.path.lstrip("/").split("/")[0]

    if "youtube.com" in host:
        if parsed.path == "/watch":
            query = parse_qs(parsed.query)
            if "v" in query and query["v"]:
                return query["v"][0]
        path_parts = [part for part in parsed.path.split("/") if part]
        if len(path_parts) >= 2 and path_parts[0] in {"embed", "shorts"}:
            return path_parts[1]

    raise ValueError("Could not extract a valid YouTube video ID.")


def fetch_transcript_text(video_id: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join(part["text"].strip() for part in transcript if part.get("text"))
    if not text:
        raise ValueError("Transcript is empty or unavailable.")
    return text


class YouTubeRAGChatbot:
    def __init__(self, cohere_api_key: Optional[str] = None, persist_directory: str = "./chroma_db") -> None:
        self.cohere_api_key = cohere_api_key or os.getenv("COHERE_API_KEY")
        if not self.cohere_api_key:
            raise ValueError("COHERE_API_KEY is required.")
        self.persist_directory = persist_directory
        self.qa_chain = None

    def ingest_video(self, video: str) -> None:
        from langchain.chains import RetrievalQA
        from langchain.schema import Document
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        from langchain_community.vectorstores import Chroma
        from langchain_cohere import ChatCohere, CohereEmbeddings

        video_id = extract_video_id(video)
        transcript_text = fetch_transcript_text(video_id)

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = splitter.split_text(transcript_text)
        docs = [Document(page_content=chunk, metadata={"video_id": video_id}) for chunk in chunks]

        embeddings = CohereEmbeddings(cohere_api_key=self.cohere_api_key, model="embed-english-v3.0")
        vectorstore = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=self.persist_directory,
            collection_name=f"youtube_{video_id}",
        )
        vectorstore.persist()

        llm = ChatCohere(cohere_api_key=self.cohere_api_key, model="command-r-plus", temperature=0)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        )

    def ask(self, question: str) -> str:
        if self.qa_chain is None:
            raise RuntimeError("No video has been ingested yet.")
        response = self.qa_chain.invoke({"query": question})
        return response["result"]


def main() -> None:
    parser = argparse.ArgumentParser(description="YouTube RAG chatbot using LangChain, Cohere and ChromaDB.")
    parser.add_argument("--video", required=True, help="YouTube URL or video ID")
    args = parser.parse_args()

    bot = YouTubeRAGChatbot()
    bot.ingest_video(args.video)

    print("Chatbot is ready. Ask questions about the video. Type 'exit' to quit.")
    while True:
        question = input("> ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        print(bot.ask(question))


if __name__ == "__main__":
    main()
