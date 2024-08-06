import os
from dotenv import load_dotenv
load_dotenv()


from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


## prompt TEmmpelete
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful AI assistant that can help me with my questions"),
        ("user","questions:{question}")

    ]
)


##streamlit framework

st.title("langchain demo with gemma 2")
input_text=st.text_input("what question you have in mind")

#oolama 2
llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
   st.write(chain.invoke({"question":input_text})) 

