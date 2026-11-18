# AI Powered Website Link Analysis

**A Python application that accepts a website URL, extracts its publicly accessible HTML content, analyzes the content using the Groq API, and displays business, competitor, SEO, service, and target-audience insights in a browser.
The project uses FastAPI for the backend and a simple HTML, CSS, and JavaScript page for the frontend.**

## Tech Stack 
 - Python
 - Fastapi
 - BeautifulSoup4 (website content extraction)
 - HTMl
 - Groq AI
 
## Features
- Accepts a website URL through an HTML form.
- Validates the URL using Pydantic and checks the URL scheme.
- Fetches website HTML using HTTPX.
- Extracts the page title, meta description, and readable text using BeautifulSoup.
- Sends cleaned website content to a Groq-hosted language model.
- Requests a JSON response containing five website-analysis sections.
- Displays the response dynamically as HTML cards.
- Shows loading and error messages in the frontend.

 ## Application Workflow
```
   User enters a website URL
          |
          v
HTML / CSS / JavaScript frontend
          |
          | POST /link-analysis
          v
FastAPI backend
          |
          v
URL validation
          |
          v
HTTPX fetches the website HTML
          |
          v
BeautifulSoup extracts and cleans text
          |
          v
Groq API analyzes the extracted content
          |
          v
Groq returns JSON
          |
          v
FastAPI returns the JSON response
          |
          v
JavaScript displays the five analysis sections
```
## Project Structure
```
ai-link-analysis/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   │
│   ├── services/
│   │   ├── website_extractor.py
│   │   └── llm_service.py
│   │
│   └── templates/
│       └── index.html
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
### Installation
1. Clone the repository
```
   git clone https://github.com/shijuavtm-sudo/Website-Link-Analysis.git
   cd ai-link-analysis
```
If you have not created a GitHub repository yet, create the project folder locally and open it in VS Code.
2. Create a virtual environment
```
python -m venv venv
```
A virtual environment keeps this project's dependencies separate from other Python projects.
3. Activate the virtual environment
Windows --- Command Prompt:
```
venv\Scripts\activate
```
Windows --- PowerShell:
```
.\venv\Scripts\Activate.ps1
```
Linux, macOS, or GitHub Codespaces:
```
source venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
### Environment Configuration
The application requires a Groq API key.
1. Create a Groq API key
```
Visit the Groq Console.
Sign in or create an account.
Open the API keys section.
Generate an API key.
Copy the key and keep it private.
```
2. Create the .env file
Create .env in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```
The model value is an example configuration. Confirm that the model is currently available to your Groq account before running the application.
3. Create .env.example
Commit this example file to GitHub, but never commit your real .env file.
```
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```
5. Configure .gitignore
Make sure the following entries are present:
```
venv/
.env
__pycache__/
*.pyc
.pytest_cache/
```
### Run the Application
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 4000
```
Url:: http://localhost:4000
