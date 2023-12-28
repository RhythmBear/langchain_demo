import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv['OPENAI_API_KEY']

# Create Basic Syntax for application
st.title("📜🪛 Website Scraper")
prompt = st.text_input("Enter In URL of Website")


# Create a Prompt Template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Write me a youtube video title about {topic}'
)

# LLMS
gpt = OpenAI(temperature=0.5)
title_chain = LLMChain(llm=gpt, prompt=title_template, verbose=True)


if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)