# Gemini LLM Application

This Streamlit application leverages Google's Gemini Pro and Gemini Pro Vision models to generate text and image responses.

## Features

* **Text-only mode:** Get text responses from the Gemini Pro language model based on your input.
* **Image and text mode:** Include an optional image with your text prompt to receive image-based or multi-modal responses using Gemini Pro Vision.

## Setup

1. **Environment Variables:** Create a `.env` file in your project directory and add your Google API key:

GOOGLE_API_KEY=your_api_key_here

2. **Install Dependencies:**
```bash
pip install streamlit google-generativeai python-dotenv pillow 

How to Run
Activate environment (if applicable): source venv/bin/activate
Start the application: streamlit run app.py
Open in your browser: Navigate to the URL shown in your terminal (usually http://localhost:8501).
Choose a mode and provide input.
Click "Submit" to see the model's response.


Code Explanation
get_response(input_text, image): This function intelligently selects the correct Gemini model based on whether an image is provided.
Streamlit App: The Streamlit interface provides a user-friendly way to interact with the models, including:
Mode selection: Dropdown to choose between text-only or image+text input.
Input fields: Text area for text input, and a file uploader for images (if needed).
Output: Displays the model's response in a clear format.****


Tips
Image types: Supported formats include JPG, JPEG, and PNG.
Response time: Responses can take a few seconds to generate, especially for complex prompts or large images.
Gemini model capabilities: Explore the full potential of Gemini models in Google's documentation for a wider range of use cases.
API limitations: Be aware of the Google Generative AI API's usage limits.


Disclaimer
This project demonstrates the use of Google Gemini models for educational and experimental purposes.
Always refer to Google's official documentation and terms of service for the most accurate and up-to-date information.

