from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini model
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = "Q&A Demo")
st.header("Gemini LLM Applicaiton")
input = st.text_input("Input: ",key = "input")
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)
    
