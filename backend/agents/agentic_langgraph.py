from langgraph.graph import StateGraph, END
from typing import TypedDict

from backend.agents.router_agent import route_query
from backend.agents.retriever_agent import retrieve_docs
from backend.agents.response_agent import generate_answer
from backend.agents.evaluator_agent import evaluate_answer
from backend.tools.ticket_tool import create_support_ticket


class AgentState(TypedDict):
    query: str
    domain: str
    docs: list
    answer: str
    confidence: float
    ticket: dict


def router_node(state):
    state["domain"] = route_query(state["query"])
    return state


def retriever_node(state):
    docs = retrieve_docs(state["query"])
    state["docs"] = docs
    return state


def response_node(state):
    answer = generate_answer(state["query"], state["docs"])
    state["answer"] = answer
    return state


def evaluator_node(state):
    score = evaluate_answer(
    state["query"],
    state["answer"],
    state["docs"]
)
    state["confidence"] = score
    return state


def ticket_node(state):
    if state["confidence"] < 0.6:
        ticket = create_support_ticket.invoke({"query": state["query"]})
        state["ticket"] = ticket

    else:
        state["ticket"] = None
    return state

def decision_edge(state):
    if state["confidence"] < 0.6:
        return "ticket"
    return END


graph = StateGraph(AgentState)

graph.add_node("router", router_node)
graph.add_node("retriever", retriever_node)
graph.add_node("response", response_node)
graph.add_node("evaluator", evaluator_node)
graph.add_node("ticket", ticket_node)

graph.set_entry_point("router")
graph.add_edge("router", "retriever")
graph.add_edge("retriever", "response")
graph.add_edge("response", "evaluator")

graph.add_conditional_edges(
    "evaluator",
    decision_edge,
    {
        "ticket": "ticket",
        END: END
    }
)

graph.add_edge("ticket", END)
app_graph = graph.compile()

def run_agentic_graph(query):
    result = app_graph.invoke({"query": query})
    return result

