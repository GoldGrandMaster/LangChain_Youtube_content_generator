# Bring in deps
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
# print(OPENAI_API_KEY)
# App framework
st.title('YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'write me a youtube video script based on this title TITLE: {title}'
)

# LLMs
llm = OpenAI(temperature = 0.9)
title_chain = LLMChain(llm = llm, prompt = title_template, verbose = True, output_key = 'title')
script_chain = LLMChain(llm = llm, prompt = script_template, verbose = True, output_key = 'script')
sequential_chain = SequentialChain(chains = [title_chain, script_chain], input_variables = ['topic'], output_variables = ['title', 'script'], verbose = True)

# Show stuff to the screen if there's a prompt
if prompt:
    response = sequential_chain({'topic' : prompt})
    st.write(response['title'])
    st.write(response['script'])
