from fastapi import FastAPI
from pydantic import BaseModel

from backend.guardrails.security import detect_prompt_injection
from backend.agents.agentic_langgraph import run_agentic_graph


app = FastAPI()

class Query(BaseModel):
    query: str


@app.post("/ask")
def ask(q: Query):

    if detect_prompt_injection(q.query):

        return {
            "error": "Prompt injection detected. Request blocked."
        }

    result = run_agentic_graph(q.query)

    return result