from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

st.header("Research Tool")

user_input = st.text_input("Enter your query:")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)