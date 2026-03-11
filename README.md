**BCG Multi-Agent Support Assistant (Multi Agent and RAG)**

This project implements an enterprise AI support agent capable of answering employee policy questions and escalating unresolved issues by creating support tickets.
The system uses multi-agent orchestration with LangGraph, Retrieval-Augmented Generation (RAG), and tool-based reasoning.

**Project Architecture**

The system consists of multiple specialized AI agents working together:

User Query-> Guardrail Agent-> Router Agent-> Retriever Agent (RAG)-> Response Agent-> Evaluator Agent-> Ticket Tool (if low confidence)

**Features**

1. Multi-agent architecture using LangGraph
2. Retrieval-Augmented Generation using Chroma Vector DB
3. Domain routing for HR, IT, Finance
4. Guardrails for prompt injection detection
5. Tool use for automatic ticket creation
6. Confidence scoring for response evaluation

**FastAPI backend + Streamlit UI**

How to Run Locally
1. Clone Repository

      git clone https://github.com/rc2007/agentic-bcg-support-agent.git

      cd agentic-bcg-support-agent

2. Create Virtual Environment
   
      python -m venv venv

    For Linux

      source venv/bin/activate

    Windows

      venv\Scripts\activate

3. Install Dependencies
   
      pip install -r requirements.txt

4. Configure Environment Variables
   
      Replace OPEN_API_KEY with your API key.

      OPENAI_API_KEY=<your_openai_key>

5. Ingest Documents into Vector Database

      python ingest.py

      This will:
      
      Load HR, IT, and Finance policy documents
      
      Chunk the documents
      
      Generate embeddings
      
      Store vectors in Chroma DB
      
6. Run Backend

      uvicorn backend.main:app --reload
      
      Backend will start at

      http://localhost:8000

7. Run Frontend

      streamlit run frontend/streamlit_app.py
      
      UI will open at

      http://localhost:8501

**Example Queries**

Policy Questions

How do I submit an expense claim?

What is the work from home policy?

How many leave days do employees get?

IT Issues

My laptop keeps crashing

I cannot access the VPN

If the system cannot confidently answer, it creates a support ticket automatically.


**Technology Stack**

**LLM**	-->  OpenAI

**Orchestration** -->  LangGraph

**Retrieval**	-->  LangChain + Chroma

**Backend** -->  FastAPI

**UI**-->	 Streamlit

**Deployment** -->	 Render + Streamlit Cloud
