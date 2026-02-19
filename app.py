

import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load env variables
load_dotenv()

# Safety check 
if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY not found. Check your .env file.")
    st.stop()

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "{question}")
    ]
)

# UI
st.title("LangChain Chatbot (GPT-4o-mini)")
question = st.text_input("Ask your question")

# LLM
llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = prompt | llm | parser

if question:
    st.write(chain.invoke({"question": question}))
