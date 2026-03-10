from langchain_openai import ChatOpenAI
from backend.config import Config

llm = ChatOpenAI(model=Config.LLM_MODEL, temperature=0)

def generate_answer(query, docs):

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an enterprise support assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{query}

Answer clearly.
"""

    response = llm.invoke(prompt)

    return response.content