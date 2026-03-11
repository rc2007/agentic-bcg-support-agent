Command to ingest:

python ingest.py

FOR LOCAL SETUP:

Start backend
uvicorn backend.main:app --reload

Start UI
streamlit run frontend/streamlit_app.py

