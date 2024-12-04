
from flask import Flask, request,jsonify
import requests
import os
import bs4
from dotenv import load_dotenv
import googlesearch
import openai
import httpx
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
genai.configure(api_key=os.getenv("KEY"))


@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    # get the data/query from streamlit app
    query = request.get_json()
    print("Received query: ", query.get('query'))
    
    # Step 1: Search and scrape articles based on the query
    print(f"Step 1: searching articles for {query.get("query")}")
    searchResults = googlesearch.search(query.get("query"), advanced=True,num_results=4)
    # print([(result.url) for result in searchResults])


    # Step 2: Concatenate content from the scraped articles
    print("Step 2: concatenating content")
    parsed_links = []
    for search in searchResults:
        data = requests.get(search.url)
        readableData = bs4.BeautifulSoup(data.text).get_text()
        parsed_links.append(readableData)
        parsed_links.append(";")
    # Step 3: Generate an answer using the LLM
    print("Step 3: generating answer")
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "You are a website summariser, you will be fed 4 articles seperated by semicolons, \
            you have to return their summaries sorted by article number in the format # Article \\n summary. "},
            ]
        )
    response = chat.send_message(f"{[parsed_link for parsed_link in parsed_links]}")
    # return the jsonified text back to streamlit
    return response.text

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
