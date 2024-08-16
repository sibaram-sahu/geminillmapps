from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(system_prompt, image, prompt):
    """
        get gemini response from system prompt
    """
    response = model.generate_content([system_prompt, image[0], prompt])
    return response.text

def get_image_details(uploaded_file):
    """
        get the data from the invoice and retus as a list
    """
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="Gemini Application Invoice Extractor")

st.header("Gemini Application Invoice Extractor")

prompt = st.text_input("Prompt: ", key="prompt")
uploaded_file = st.file_uploader("Upload an Invoice...", type=["jpg", "jpeg", "png", "pdf"])

image = ""

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded file", use_column_width=True)

submit = st.button("Tell me about the invoice.")

system_prompt = """
You are an expert in uderstanding invoices. We will upload a image as invoice and you will have to answer any questions based on the uploaded invoice image.
"""

if submit:
    image_data = get_image_details(uploaded_file)
    final_reponse = get_gemini_response(system_prompt, image_data, prompt)
    st.subheader("The Response is ")
    st.write(final_reponse)