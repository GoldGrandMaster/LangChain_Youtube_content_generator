# Bring in deps
import os
import streamlit as st
from langchain.llms import OpenAI
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
# print(OPENAI_API_KEY)
# App framework
st.title('YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

# LLMs
llm = OpenAI(temperature = 0.9)

# Show stuff to the screen if there's a prompt
if prompt:
    response = llm(prompt)
    st.write(response)
