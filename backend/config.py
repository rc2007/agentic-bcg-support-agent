import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("OPENAI_LLM_MODEL")
    EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")