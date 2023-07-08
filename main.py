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

# from langchain import PromptTemplate

# template = """Question:{question}Answer:"""
# prompt = PromptTemplate(
#     template = template,
#     input_variables = ['question']
# )

# # user question
# question = "Which NFL team won the Super Bowl in the 2010 season?"

# import os
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = HF_API_KEY

# from langchain import HuggingFaceHub, LLMChain

# # initialize Hub LLM
# hub_llm = HuggingFaceHub(
#     repo_id = 'google/flan-t5-xl',
#     model_kwargs = {'temperature':1e-10}
# )

# # create prompt template > LLM chain
# llm_chain = LLMChain(
#     prompt = prompt,
#     llm = hub_llm
# )

# # ask the user question about NFL 2010
# print(llm_chain.run(question))