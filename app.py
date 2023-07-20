# ...............................................OPEN AI
# import os
# from apikey import apikey
# import streamlit as st
# import langchain
# from langchain.llms import OpenAI



# os.environ['OPENAI_API_KEY']=apikey

# st.title('LANFCHAIN APP')

# prompt= st.text_input('plug in your prompt')

# #llms
# llm=OpenAI(temperature=0.9)

# if prompt:
#     response= llm(prompt)
#     st.write(response)

# ...................................................OPEN AI
# import os 
# os.environ["OPENAI_API_KEY"]="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"

# from langchain.llms import OpenAI

# llm=OpenAI(temperature=0.9)
# text= "what would be a good company that makes colorful socks?"
# print(llm(text))

# ...........................................................HUGGING FACE APPROACH
import os
from apikey import apikey
import streamlit as st
from langchain import HuggingFaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

st.title('LANGCHAIN APP')

# Create the HuggingFaceHub model
llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature": 0.6, "max_length": 64})

# Prompt input field
prompt = st.text_input('Plug in your prompt')

if prompt:
    response = llm(prompt)
    generated_text = response.choices[0].text
    st.write(generated_text)
