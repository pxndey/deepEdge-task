
import streamlit as st
import requests

api_url = "http://localhost:5001/query"

st.title("LLM-based RAG Search")

# Input for user query
query = st.text_input("Enter your query:")

if st.button("Search"):
    # Make a POST request to the Flask API
    payload = {"query": query}
    response = requests.post(api_url, json=payload)
    print("accessing ", f"{api_url}", " with query ", query)
    
    # implement the flask call here
    
    if response.status_code == 200:
        # Display the generated answer
        st.markdown(response.text)
        # answer = response.json().get('answer', "No answer received.")
        # st.write("Answer:", answer)
    else:
        st.error(f"Error: {response.status_code}")
