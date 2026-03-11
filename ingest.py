import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from backend.config import Config  # must define VECTOR_DB_PATH and EMBEDDING_MODEL

load_dotenv()
DATA_PATH = "data"  # folder with .txt files


def load_documents():
    documents = []
    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_PATH, file))
            docs = loader.load()
            for doc in docs:
                doc.metadata["source"] = file
            documents.extend(docs)
    return documents


def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return text_splitter.split_documents(documents)


def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(model=Config.EMBEDDING_MODEL)
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=Config.VECTOR_DB_PATH
    )
    return vector_db


def main():
    print("Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")

    print("Splitting documents into chunks...")
    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")

    print("Creating vector store...")
    create_vector_store(chunks)
    print("Vector store created successfully!")

    print("\nSample chunk:\n")
    print(chunks[0].page_content)


if __name__ == "__main__":
    main()

