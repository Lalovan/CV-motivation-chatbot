# Anna's CV and Motivation Chatbot #
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

![Ollama](https://img.shields.io/badge/Ollama-Supported-black?logo=ollama)
![Groq API](https://img.shields.io/badge/Groq-API-orange?logo=groq)


At a Glance: 
A retrieval-grounded LLM assistant that answers questions about my CV and professional motivation to be a Data Scientist, in any language.

## 1. Introduction and Demo ##

Live app: [to be activated for specific job showcases]

Example usage: 

- "What is Anna's experience with machine learning?"
- "Wat is haar ervaring met Python?"
- "Quelle est son expérience en data science?"

<img width="700" alt="image" src="https://github.com/user-attachments/assets/29337231-251c-47e0-a1a5-3299895eef24" />


## 2. Installation and Deployment to Streamlit Cloud ##

### Prerequisites

- See requirements.txt
- Git
- A Groq API key (for LLM inference)

#### 1. Clone the Repository

```
git clone https://github.com/Lalovan/CV-motivation-chatbot.git
cd your-repo-name
```

#### 2. Create and Activate a Virtual Environment

```
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

#### 3. Install dependencies

```
pip install -r requirements.txt
```

#### 4.Configure Environment Variables (Local Testing)

Create a ```.env``` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
MY_CV_TEXT="""
Paste your CV text here.
This content will be embedded locally and used for retrieval.
"""
```
**IMPORTANT:** The ```.env``` file must **never** be committed to GitHub. It is listed in ```.gitignore```.

#### 5. Run the Application

```
streamlit run app.py
```
The app will be available at: ```http://localhost:XXXX```


#### 6. Deployment to Streamlit Cloud

This application is deployed using Streamlit Cloud, which is directly linked to the GitHub repository.
For production deployment, environment variables are securely stored in the Streamlit Secrets Manager instead of ```.env``` files.

**Deployment Workflow**

1. The source code is pushed to GitHub (without any secrets or personal data).
2. Streamlit Cloud pulls the repository and installs dependencies from `requirements.txt`.
3. Sensitive information (API keys, CV content) is injected securely via the **Streamlit Secrets Manager**.
4. The application is deployed and publicly accessible via a Streamlit-hosted URL.

This setup ensures a clear separation between:
- Code (public, version-controlled)
- Sensitive data(private, encrypted, never committed)


**Streamlit Secrets Configuration**

For deployment, the following secrets must be configured in the Streamlit Cloud dashboard:

```toml
GROQ_API_KEY = "your-groq-api-key"

MY_CV_TEXT = """
Full CV content, including experience, publications,
skills, and motivation.
"""
```

## 3. What problem does it solve? ##

Recruiters often want fast, targeted insight about a candidate’s experience and specific contribution the candidate may have to the company. 

In a creative way, this project solves that by turning my CV and carefully prepared information into an intelligent multilingual assistant that provides instant, grounded answers about my experience and general professional motivation as a Data Scientist. 

This format aims to make the exchange feel personal, to invite engagement and curiosity! As an added value, a way to show case depth of some of my skills and my enthusiasm to build solutions. 

**A few honest questions (and equally honest answers)**

- Why use an assistant at all instead of just reading the CV or talking to the candidate directly?

Nothing beats a real conversation, and this project is not trying to compete with one.
The assistant simply removes the (boring) CV reading part by answering quick, factual questions instantly so that human attention can be saved for what actually matters (discussion, interpretation, and chemistry). So let's think of it as a well-prepared introduction.

- Isn’t this automating something that should stay personal?

The chatbot uses only information that the candidate is comfortable with. Moreover, this information is safely stored and not showcased.
Job-specific motivation, nuance, and job-specific intent are very intentionally not automated. Those belong in an interview room, not in a prompt. The assistant handles consistency, availability, and multilingual access.

... And personal connection is still a human-only feature (and proudly so).


## 4. Key Features ##

- Hallucination-safe answers (CV and motivation-grounded only);
- Language-preserving response generation;
- Retrieval with embeddings (RAG);
- Fast API-based inference;
- Data protection via Streamlit Secrets;

## 5. System Architecture ##

### Components

#### 1. Streamlit Frontend
- Provides a chat-based user interface
- Displays conversation history
- Collects recruiter questions

#### 2. Secure Data Storage
- CV and personal information are stored **ONLY** in:
  - Local `.env` (development)
  - Streamlit Secrets Manager (production)
- No CV data is committed to GitHub or sent to third-party services

#### 3. Embedding & Retrieval Layer
- CV text is split into small overlapping chunks
- Chunks are embedded using `SentenceTransformers`
- FAISS performs fast vector similarity search
- Only the **top-k relevant chunks** are retrieved per query

#### 4. External LLM (Groq)
- Receives:
  - User question
  - Retrieved context chunks
- Does **NOT** receive the full CV
- Generates a concise, context-aware response

## 6. Tech Stack ##

- Language Model: llama-3.3-70b-versatile 
- Backend: Python (Ollama, Groq API)
- Frontend: Streamlit
- Embeddings
- Vector Store: FAISS 
- Safety of data is ensured by adding API keys and personal information to safety space of streamlit


## 7. Future Improvements ##
Automatic CV updates will be added in the near future. 

## 8. Timeline ##

This project took 3 days to be built. 

## 9. Contact ##

This project has been done by Anna Lalova ([LinkedIn](https://www.linkedin.com/in/anna-lalova/)), in collaboration with [Amine](https://github.com/AmineSam).

The idea has been further built on and inspired by a project of [Alfiya Khabibillina](https://huggingface.co/spaces/justalphie).
