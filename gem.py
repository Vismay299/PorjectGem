from dotenv import load_dotenv
load_dotenv()
from PIL import Image

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Gemini Models
model_text = genai.GenerativeModel("gemini-pro")
model_vision = genai.GenerativeModel("gemini-pro-vision")

def get_response(input_text, image=None):
    """Gets a response from the appropriate Gemini model."""
    if image:
        if input_text:
            return model_vision.generate_content([input_text, image]).text
        else:
            return model_vision.generate_content(image).text
    else:
        return model_text.generate_content(input_text).text


# Streamlit App
st.set_page_config(page_title="Gemini LLM Application")
st.header("Gemini LLM Application")

# Input Mode Selection
mode = st.selectbox("Choose Input Mode", ["Text Only", "Image and Text (Optional)"])

if mode == "Text Only":
    input_text = st.text_area("Enter your text:", height=150)
    image = None  # Ensure no image is processed
elif mode == "Image and Text (Optional)":
    input_text = st.text_area("Enter your text (optional):", height=150)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = Image.open(uploaded_file) if uploaded_file else None
    if image:
        st.image(image, caption="Uploaded Image.", use_column_width=True)

# Generate Response
if st.button("Submit"):
    if (mode == "Text Only" and not input_text) or (mode == "Image and Text (Optional)" and not (input_text or image)):
        st.warning("Please provide input.")
    else:
        response = get_response(input_text, image)
        st.subheader("The Response is:")
        st.write(response)
