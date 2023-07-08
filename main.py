# Bring in deps
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# from apikey import apikey

os.environ['OPENAI_API_KEY'] = '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'
# print(OPENAI_API_KEY)
# App framework
st.title('YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'write me a youtube video title about {topic}'
)

# LLMs
llm = OpenAI(temperature = 0.9)
title_chain = LLMChain(llm = llm, prompt = title_template, verbose = True   )

# Show stuff to the screen if there's a prompt
if prompt:
    response = title_chain.run(topic = prompt)
    st.write(response)
