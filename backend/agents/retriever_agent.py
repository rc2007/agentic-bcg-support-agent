from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from backend.config import Config

embeddings = OpenAIEmbeddings(model=Config.EMBEDDING_MODEL)

vectorstore = Chroma(
    persist_directory=Config.VECTOR_DB_PATH,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k":3})

def retrieve_docs(query: str):
    docs = retriever.invoke(query)
    return docs