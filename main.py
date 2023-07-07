from langchain import PromptTemplate

template = """Question:{question}Answer:"""
prompt = PromptTemplate(
    template = template,
    input_variables = ['question']
)

