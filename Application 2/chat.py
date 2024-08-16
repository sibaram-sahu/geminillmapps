from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import google.generativeai as genai
import os 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="Gemini Application Two")

st.header("Gemini Application Two")

if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []

input = st.chat_input("Say something")
# st.session_state["chat_history"].append(('AI', "Hi, How can i help you?"))

if input:
    final_response = get_gemini_response(input)

    st.session_state["chat_history"].append(('USER', input))
    message = ""
    for chunk in final_response:
        # st.write(chunk.text)
        message += chunk.text

    st.session_state["chat_history"].append(('AI', message))

for role,text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")