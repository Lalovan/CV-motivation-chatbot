# Anna's CV and Motivation Chatbot #
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

![Ollama](https://img.shields.io/badge/Ollama-Supported-black?logo=ollama)
![Groq API](https://img.shields.io/badge/Groq-API-orange?logo=groq)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

At a Glance: 
A retrieval-grounded LLM assistant that answers questions about my CV and professional motivation as a Data Scientist, in any language.

## 1. Introduction and Demo ##

Live app: https://cv-chatbot-anna-lalo.streamlit.app

Example usage: 

- "What is Anna's experience with machine learning?"
- "Wat is haar ervaring met Python?"
- "Quelle est son expérience en data science?"

## 2. Installation ##






## 3. What problem does it solve? ##

Recruiters often want fast, targeted insight about a candidate’s experience and specific contribution the candidate may have to the company. 

In a creative way, this project solves that by turning my CV and carefully prepared information into an intelligent multilingual assistant that provides instant, grounded answers about my experience and general professional motivation as a Data Scientist. 

This format aims to make the exchange feel personal, to invite engagement and curiosity! As an added value, a way to show case depth of some of my skills and my enthusiasm to build solutions. 

**A few honest questions (and equally honest answers)**

Why use an assistant at all instead of just reading the CV or talking to the candidate directly?

Nothing beats a real conversation, and this project is not trying to compete with one.
The assistant simply removes the (boring) CV reading part by answering quick, factual questions instantly so that human attention can be saved for what actually matters (discussion, interpretation, and chemistry). So let's think of it as a well-prepared introduction.

Isn’t this automating something that should stay personal?

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

XXXXXXXXXXX

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
