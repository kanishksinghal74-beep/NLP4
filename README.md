# 🤖 NLP Linguistic Analysis Dashboard

A Natural Language Processing dashboard built using **Python, FastAPI, spaCy, NLTK, and Gradio**.

The application provides an interactive interface for performing different NLP and linguistic analysis operations on user-provided text.

---

## 🚀 Features

The dashboard supports the following operations:

- 🏷️ Named Entity Recognition (NER)
- 🔗 Named Entity Relationship
- 📝 POS Tagging
- 📊 POS Distribution
- 🔤 Lemmatization
- 🌱 Stemming
- 🧬 Morphology
- 🌳 Dependency Parsing

The project also provides:

- Interactive Gradio frontend
- FastAPI REST API
- Swagger/OpenAPI documentation
- Health check endpoint
- Docker support
- GitHub integration
- Railway deployment

---

# 🌐 Live Deployment

## 🖥️ Gradio Dashboard

**Live Application:**

https://nlp-linguistic-dashboard-production.up.railway.app/

Use this link to access the complete NLP dashboard.

---

## 📚 FastAPI Swagger Documentation

**API Documentation:**

https://nlp-linguistic-dashboard-production.up.railway.app/docs

The Swagger interface can be used to view and test the available API endpoints.

---

## ❤️ Health Check

**Health Endpoint:**

https://nlp-linguistic-dashboard-production.up.railway.app/health

---

# 🧠 NLP Operations

## 1. Named Entity Recognition

Identifies entities present in the input text.

Examples:

```text
Microsoft → ORG
Bill Gates → PERSON
California → GPE
```

---

## 2. Named Entity Relationship

Identifies relationships between entities occurring within the same sentence.

Example:

```text
Microsoft → Bill Gates
Bill Gates → California
```

---

## 3. POS Tagging

Identifies the Part-of-Speech tag for every token.

Example:

```text
Microsoft → PROPN
was → AUX
founded → VERB
by → ADP
Bill → PROPN
Gates → PROPN
```

---

## 4. POS Distribution

Provides the frequency/distribution of POS tags in the input text.

Example:

```text
PROPN → 4
ADP   → 2
AUX   → 1
VERB  → 1
```

---

## 5. Lemmatization

Converts words into their base/dictionary form.

Example:

```text
was → be
founded → found
```

---

## 6. Stemming

Reduces words to their stem/root form.

Example:

```text
founded → found
Gates → gate
```

---

## 7. Morphology

Provides morphological information about tokens.

Examples:

```text
Number=Sing
Tense=Past
VerbForm=Part
Person=3
Mood=Ind
```

---

## 8. Dependency Parsing

Identifies grammatical relationships between words.

Examples:

```text
nsubjpass
auxpass
ROOT
agent
compound
pobj
prep
punct
```

The application also generates a dependency parsing visualization using spaCy's dependency rendering.

---

# 📁 Project Structure

```text
NLP(E5)/
│
├── api1.py
├── app1.py
├── model1.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

### File Description

### `model1.py`

Contains the main NLP processing logic.

It performs:

- Named Entity Recognition
- Entity Relationships
- POS Tagging
- POS Distribution
- Lemmatization
- Stemming
- Morphology
- Dependency Parsing

---

### `app1.py`

Contains the **Gradio frontend dashboard**.

---

### `api1.py`

Contains the **FastAPI backend** and connects the API with the Gradio application.

---

### `requirements.txt`

Contains all Python dependencies required by the project.

---

### `Dockerfile`

Used to containerize the application and deploy it on Railway.

---

### `.gitignore`

Contains files and folders that should not be uploaded to GitHub, such as the Python virtual environment.

---

# 🛠️ Technologies Used

- **Python**
- **FastAPI**
- **Gradio**
- **spaCy**
- **NLTK**
- **Uvicorn**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Docker**
- **Git**
- **GitHub**
- **Railway**

---

# 💻 Local Setup

Follow these steps if you want to run the project on another computer.

## Step 1 — Check Python

Open Command Prompt and run:

```cmd
python --version
```

---

## Step 2 — Clone the Repository

```cmd
git clone https://github.com/MarGiN-7/nlp-linguistic-dashboard.git
```

Then enter the project folder:

```cmd
cd nlp-linguistic-dashboard
```

---

## Step 3 — Create Virtual Environment

```cmd
python -m venv venv
```

---

## Step 4 — Activate Virtual Environment

For Windows CMD:

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of the command prompt.

---

## Step 5 — Upgrade pip

```cmd
python -m pip install --upgrade pip
```

---

## Step 6 — Install Requirements

```cmd
pip install -r requirements.txt
```

---

## Step 7 — Install spaCy English Model

This step is required for the NLP analysis.

```cmd
python -m spacy download en_core_web_sm
```

After successful installation, you should see a message similar to:

```text
Successfully installed en-core-web-sm
```

---

# 🧪 Test the NLP Model

Before starting the application, test `model1.py`.

Run:

```cmd
python -c "from model1 import analyze_text; print(analyze_text('Microsoft was founded by Bill Gates in California.'))"
```

A successful result should contain:

```text
statistics
tokens
entities
relationships
pos_distribution
dependencies
```

---

# ▶️ Run the Application Locally

Start the FastAPI server using:

```cmd
python -m uvicorn api1:app --host 127.0.0.1 --port 7860
```

Open the following URL in your browser:

```text
http://127.0.0.1:7860
```

The Gradio dashboard should now be available.

---

# 📚 Test Swagger Documentation Locally

Open:

```text
http://127.0.0.1:7860/docs
```

This opens the FastAPI Swagger UI.

You can use Swagger to view and test the API endpoints.

---

# 🔗 API Endpoints

## Root Endpoint

```http
GET /
```

Local:

```text
http://127.0.0.1:7860/
```

---

## Health Check

```http
GET /health
```

Local:

```text
http://127.0.0.1:7860/health
```

---

## Analyze Text

```http
POST /api/analyze
```

Example request:

```json
{
  "text": "Microsoft was founded by Bill Gates in California."
}
```

The API returns NLP information including:

- Statistics
- Tokens
- Named Entities
- Entity Relationships
- POS Distribution
- Dependencies

---

# 🐙 GitHub Setup

If you are creating the GitHub repository for the first time, open Command Prompt inside the project folder.

## Step 1 — Initialize Git

```cmd
git init
```

---

## Step 2 — Check Git Status

```cmd
git status
```

---

## Step 3 — Add All Project Files

```cmd
git add .
```

---

## Step 4 — Create First Commit

```cmd
git commit -m "Initial NLP linguistic dashboard"
```

---

## Step 5 — Rename Branch to Main

```cmd
git branch -M main
```

---

## Step 6 — Connect GitHub Repository

Replace the URL with your own GitHub repository URL:

```cmd
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

---

## Step 7 — Push to GitHub

```cmd
git push -u origin main
```

Your project should now be available on GitHub.

---

# 🔄 Updating the GitHub Repository

Whenever you make changes to the project, use:

```cmd
git status
```

Then:

```cmd
git add .
```

Then commit:

```cmd
git commit -m "Update NLP dashboard"
```

Finally:

```cmd
git push
```

---

# 🔍 Check GitHub Remote

To check which GitHub repository is connected:

```cmd
git remote -v
```

If the correct repository is already connected, simply use:

```cmd
git push
```

Do not run `git remote add origin` again.

---

# 🚂 Railway Deployment

The project can be deployed publicly using **Railway**.

The deployment flow is:

```text
Local Project
     ↓
GitHub
     ↓
Railway
     ↓
Docker Build
     ↓
FastAPI + Gradio
     ↓
Public URL
```

---

# 🚀 Deploy Using Railway

## Step 1 — Push Latest Code to GitHub

Before deploying, make sure the latest version is on GitHub.

```cmd
git add .
```

```cmd
git commit -m "Prepare project for deployment"
```

```cmd
git push
```

---

## Step 2 — Open Railway

Go to:

```text
https://railway.app/
```

Create a new Railway project.

---

## Step 3 — Deploy from GitHub

Select:

```text
New Project
     ↓
Deploy from GitHub Repo
     ↓
Select Repository
```

Select:

```text
nlp-linguistic-dashboard
```

Railway will use the project's `Dockerfile` to build the application.

---

# ⚙️ Railway Start Command

If Railway asks for a custom start command, use:

```text
uvicorn api1:app --host 0.0.0.0 --port $PORT
```

Important:

```text
--host 0.0.0.0
```

must be used for production deployment.

Railway provides the production port through:

```text
$PORT
```

Do not use:

```text
127.0.0.1
```

for the Railway production server.

---

# 🌍 Generate Railway Public Domain

After the deployment succeeds:

```text
Railway Service
      ↓
Settings
      ↓
Networking
      ↓
Public Networking
      ↓
Generate Domain
```

Railway will generate a public URL similar to:

```text
https://your-project-production.up.railway.app
```

---

# 🧪 Test the Deployed Application

After Railway deployment is complete, test:

## Gradio Dashboard

```text
https://YOUR-DOMAIN/
```

## Swagger

```text
https://YOUR-DOMAIN/docs
```

## Health Check

```text
https://YOUR-DOMAIN/health
```

---

# 🔄 Railway + GitHub Automatic Deployment

Once Railway is connected to GitHub, the normal workflow becomes:

```text
Modify Code
     ↓
Test Locally
     ↓
git add .
     ↓
git commit
     ↓
git push
     ↓
GitHub
     ↓
Railway automatically deploys
     ↓
Updated Public Application
```

---

# 🐳 Docker

The project includes a `Dockerfile` so that the application can be packaged into a Docker container.

The Docker container contains the environment required to run:

```text
FastAPI
Gradio
spaCy
NLTK
Python
```

Railway uses the Docker configuration when building the deployed application.

---

# 🚨 Common Problems

## 1. spaCy Model Not Found

Run:

```cmd
python -m spacy download en_core_web_sm
```

---

## 2. Virtual Environment Not Activated

Run:

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

---

## 3. Git Remote Already Exists

If you see:

```text
error: remote origin already exists
```

check the current remote:

```cmd
git remote -v
```

If it is correct, simply run:

```cmd
git push
```

---

## 4. Nothing to Commit

Run:

```cmd
git status
```

If everything is already committed, simply use:

```cmd
git push
```

---

## 5. Railway Cannot Detect a Port

Make sure the production command uses:

```text
uvicorn api1:app --host 0.0.0.0 --port $PORT
```

Do not use:

```text
uvicorn api1:app --host 127.0.0.1 --port 7860
```

for Railway production.

---

# 📋 Complete Command Cheat Sheet

## New Computer

```cmd
git clone https://github.com/MarGiN-7/nlp-linguistic-dashboard.git
```

```cmd
cd nlp-linguistic-dashboard
```

```cmd
python -m venv venv
```

```cmd
venv\Scripts\activate
```

```cmd
python -m pip install --upgrade pip
```

```cmd
pip install -r requirements.txt
```

```cmd
python -m spacy download en_core_web_sm
```

---

## Test

```cmd
python -c "from model1 import analyze_text; print(analyze_text('Microsoft was founded by Bill Gates in California.'))"
```

---

## Run Locally

```cmd
python -m uvicorn api1:app --host 127.0.0.1 --port 7860
```

Open:

```text
http://127.0.0.1:7860
```

Swagger:

```text
http://127.0.0.1:7860/docs
```

---

## First GitHub Push

```cmd
git init
```

```cmd
git branch -M main
```

```cmd
git add .
```

```cmd
git commit -m "Initial NLP linguistic dashboard"
```

```cmd
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

```cmd
git push -u origin main
```

---

## Future Updates

```cmd
git status
```

```cmd
git add .
```

```cmd
git commit -m "Update NLP dashboard"
```

```cmd
git push
```

---

# 📌 Important Files

Make sure the repository contains:

```text
api1.py
app1.py
model1.py
requirements.txt
Dockerfile
.gitignore
README.md
```

Do **not** upload:

```text
venv/
__pycache__/
*.pyc
```

These should be excluded using `.gitignore`.

---

# 🎯 Project Workflow

```text
                 NLP LINGUISTIC DASHBOARD
                           │
                           ▼
                    Gradio Frontend
                           │
                           ▼
                      FastAPI API
                           │
                           ▼
                       model1.py
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
       NER                POS             Lemmatization
        │                  │                  │
        ▼                  ▼                  ▼
 Relationships       POS Distribution       Stemming
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                       Morphology
                           │
                           ▼
                  Dependency Parsing
                           │
                           ▼
                    Analysis Results
```

---
