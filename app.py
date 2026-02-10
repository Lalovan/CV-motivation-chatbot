import os
import faiss
import textwrap
import numpy as np
from groq import Groq
import streamlit as st
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Streamlit secrets

cv_text = st.secrets["MY_CV_TEXT"]
api_key = st.secrets["GROQ_API_KEY"]

if not api_key:
    raise RuntimeError("GROQ_API_KEY not set in environment.")

client = Groq(api_key=api_key)

# Semantic splitting of the CV and motivation information into chunks

text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
cv_chunks = text_splitter.split_text(cv_text)

# Encoding the chunks (turning text into vectors)

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
chunk_embeddings = model.encode(cv_chunks)

# FAISS Vector Search

dimension = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)   # L2 distance (Eucledian) for cosine similarity (angle between vectors: 1 = same direction, 0 = orthogonal, -1 = opposite)
index.add(np.array(chunk_embeddings))

# Retrieving

def retrieve(query, k=6): # Adaptable
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb), k)
    retrieved_chunks = [cv_chunks[i] for i in indices[0]]
    return retrieved_chunks

# Building the prompt to the LLM

def build_prompt(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are the assistant representing an AI and Machine Learning Data Science job candidate (me) and answering questions from recruiters (about her CV, overall motivation, and other background information).
Answer ONLY using the information in the context.
If there are web links provided in a related part, provide also the links in your replies. 
Format your reply in short, readable paragraphs (1-4 sentences each paragraph).
Limit your answer to a maximum of ~130 words and 2 paragraphs maximum.
If an answer is not found in the context, clearly say that the information is not available and recommend referring directly to Anna by using the contact information provided.
If a recruiter asks about a skill not mentioned in the resume, explain how quickly Anna would be able to learn it based on what is in the context.
This chatbot is made by Anna.

Context:
{context}

Question: {query}

Answer in the same language as the question.
"""
    return prompt

# Send only the 6 most relevant chunks to the Groq API 
def groq_answer(question):
    retrieved = retrieve(question)
    prompt = build_prompt(question, retrieved)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful CV assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


#------------------------------------
#           Streamlit CSS
#------------------------------------

st.set_page_config(page_title="Anna's CV and Motivation Assistant", layout="wide")

# Sidebar
with st.sidebar:
    st.title("Anna's CV Bot")

    st.markdown("""
    **Example Questions (non-exhaustive list)**
    - What work experience does Anna have?
    - What programming languages does Anna know?
    - What soft skills does Anna have?
    - What experience does she have with Machine Learning?
    - Why should I hire Anna as a Data Scientist?
    """)

    st.markdown("---")
    st.subheader("Contact")
    st.markdown("""
    
    **LinkedIn:** 
    """)

# Main Area
st.title("Talk with Anna’s CV and Motivation Assistant")

st.markdown("""
This assistant helps recruiters learn about Anna’s background, CV, experience,
and general motivation as a Data Scientist, based strictly on her uploaded information. 
            

Should you have additional questions or find the infromation here not satisfying, please contact her via the provided contact information.

            
You can ask the Assistant questions in any language, including EN, NL, FR.   
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input at the bottom
user_query = st.chat_input("Ask something about Anna's CV, motivation...")

if user_query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_query})

# Generate answer

    answer = groq_answer(user_query)

# Store assistant reply
    st.session_state.messages.append({"role": "assistant", "content": answer})

# To display all messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
   
