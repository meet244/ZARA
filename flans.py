import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv
# from transformers import T5Tokenizer, T5ForConditionalGeneration
load_dotenv()
# tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl", model_kwargs={"max_new_tokens":1200})
# model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl")

def classify(sentence):
    template = "start software / code / math / gk / wikipedia / unit conversion / alarm / timer / song or music / weather / news / navigation / conversation / others. among the given topics classify the following sentence('{question}') to one of them with possibility from 0 to 100. give response in 1-2 words."
            
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm=HuggingFaceHub(repo_id="google/flan-t5-xxl")

    llm_chain=LLMChain(
    llm=llm,
    prompt=prompt
)

    # def generate_response(question, llm_chain):
    response = llm_chain.run(sentence)
    print(response)
    return response

def response(sentence):
    template = "{question}"
            
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm=HuggingFaceHub(repo_id="google/flan-t5-xxl")

    llm_chain=LLMChain(
                    llm=llm,
                    prompt=prompt
                )

    # def generate_response(question, llm_chain):
    response = llm_chain.run(sentence)
    return response

def Mathresponse(sentence):
    template = "{question}"
            
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm=HuggingFaceHub(repo_id="google/flan-t5-xxl")

    llm_chain=LLMChain(
                    llm=llm,
                    prompt=prompt
                )

    # def generate_response(question, llm_chain):
    response = llm_chain.run(sentence)
    return response
