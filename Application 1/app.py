from dotenv import load_dotenv

# Load all the env
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
# load the api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# initialize gemini app

model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(question, image):
    if image:
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(question)
    return response.text


# start stream lit

st.set_page_config(page_title="Application One")

st.header("Gemini Application One")

input = st.text_input("Input ", key="input")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)
    
submit = st.button("Aks the question")

if submit:
    final_response = get_gemini_response(input, image)
    st.subheader("The response is ")
    st.write(final_response)