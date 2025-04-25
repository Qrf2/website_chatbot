import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Website Chatbot", layout="centered")
st.title("🤖 AI Website Chatbot Generator")
st.markdown("Embed this chatbot on your website to assist visitors.")

openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.api_base = st.secrets["OPENAI_BASE_URL"]

st.markdown("### 💬 Ask the chatbot anything!")
user_input = st.text_input("You:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Updated model name
                messages=[
                    {"role": "system", "content": "You are a helpful website assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.markdown(f"**Bot:** {response.choices[0].message.content}")
        except openai.error.OpenAIError as e:
            st.error(f"An error occurred: {e}")