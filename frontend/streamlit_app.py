import streamlit as st
import requests

st.title("BCG Multi-Agent Support Assistant")

query = st.text_input("Ask your question")

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"query": query}
    )

    data = response.json()

    st.write("Response:")

    st.json(data)