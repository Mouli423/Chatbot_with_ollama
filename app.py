import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# import os
# from dotenv import load_dotenv
# load_dotenv()

# #Langsmith tracing

# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_PROJECT"]="Streamlit practicing application"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system"," You are a helpful ai assistant. Please respond to the use queries"),
        ("user","Question:{question}")
    ]
)


def generate_response(question,llm):
    llm=OllamaLLM(model=llm)
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer=chain.invoke({"question":question})
    return answer

st.title("Streamlit Web application Practice ")

llm=st.sidebar.selectbox("select open source model",["gemma3:1b","llama3:latest"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=200)


st.write(" Go ahead and ask any question")

user_input=st.text_input("You:")


if user_input:

    response=generate_response(user_input,llm)
    st.write(response)
else:
    st.write("please provide the user input")




