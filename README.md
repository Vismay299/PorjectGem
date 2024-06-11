# Gemini LLM Application

This Streamlit application leverages Google's Gemini Pro and Gemini Pro Vision models to generate text and image responses.

## Features

* **Text-only mode:** Get text responses from the Gemini Pro language model based on your input.
* **Image and text mode:** Include an optional image with your text prompt to receive image-based or multi-modal responses using Gemini Pro Vision.

## Setup

1. **Environment Variables:** Create a `.env` file in your project directory and add your Google API key:

GOOGLE_API_KEY=your_api_key_here

2. **Install Dependencies:**
```pip install streamlit google-generativeai python-dotenv pillow ```

How to Run:
1. **Activate environment** (if applicable): `source venv/bin/activate`
2. Start the application: `streamlit run app.py`
3. Open in your browser: Navigate to the URL shown in your terminal (usually http://localhost:8501).
4. Choose a mode and provide input.
5. Click "Submit" to see the model's response.

Code Explanation:
* `get_response(input_text, image)`: This function intelligently selects the correct Gemini model based on whether an image is provided.
* Streamlit App: The Streamlit interface provides a user-friendly way to interact with the models, including:
* Mode selection: Dropdown to choose between text-only or image+text input.
* Input fields: Text area for text input, and a file uploader for images (if needed).
* Output: Displays the model's response in a clear format.

# Url For the Website
- https://vismay299-porjectgem-gem-7hdzno.streamlit.app/
