
from flask import Flask, request,jsonify
import os
import beautifulsoup as bs
from dotenv import load_dotenv
from googlesearch import search

# Load environment variables from .env file
load_dotenv()





app = Flask(__name__)


@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    # get the data/query from streamlit app
    query = request.get_json()
    print("Received query: ", query)
    
    # Step 1: Search and scrape articles based on the query
    print("Step 1: searching articles")
    searchResults = search("Google", advanced=True)
    

    # Step 2: Concatenate content from the scraped articles
    print("Step 2: concatenating content")

    # Step 3: Generate an answer using the LLM
    print("Step 3: generating answer")

    # return the jsonified text back to streamlit
    return jsonify({"Query":query['query']})

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
