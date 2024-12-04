# deepEdge-task

## Setup

- Clone the Repository
```bash
git clone https://github.com/pxndey/deepEdge-task
cd deepEdge-task
```

- Create and activate the virtual environment
```bash
python -m venv venv
venv/Scripts/activate
```

- Install required Dependencies from the root folder
```bash
pip install -r requirements.txt
```

- Add an environment file (*.env*) in the backend directory of the project with your Gemini API key in the following format:

```text
KEY=<API_KEY>
```

## Running Backend

- Navigate to backend directory
```bash
cd backend
```

- Run the Flask app
```bash
python app.py
```

## Running Frontend

- In a new terminal, activate the virtual environment and navigate to the frontend directory
```bash
venv/Scripts/activate
cd frontend
```

- Run the frontend app
```bash
streamlit run app.py
```

### Usage

- Navigate to http://localhost:8501 to view and use the deployed app

### Differences from Task

- Google's Gemini API was used in replacement of OpenAI API
- The model used was *gemini-1.5-flash*
- The *googlesearch-python*  Library was used to return top 4 webpages with keywords passed into the frontend
- All remaning requirements remain the same.
