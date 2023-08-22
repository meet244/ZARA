import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv
# from transformers import T5Tokenizer, T5ForConditionalGeneration
load_dotenv()
# tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl", model_kwargs={"max_new_tokens":1200})
# model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl")

def classify(sentence):
    template = "start software / code / math / gk / unit conversion / alarm / timer / song or music / weather / news / navigation / conversation / others. among the given topics classify the following sentence('{question}') to one of them with possibility from 0 to 100. give response in 1-2 words."
            
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

    # def get_text():
    #     # input_text = st.text_input("You: ", "", key="input")
    #     input_text = input("hi :")
    #     return input_text

def Mathresponse(sentence):
    template = "{question}\nWrite Your Final Answer. Read and Understand the Problem. Identify the Relevant Concepts. Make the equation. Perform Calculations"
            
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm=HuggingFaceHub(repo_id="google/flan-t5-xxl")

    llm_chain=LLMChain(
                    llm=llm,
                    prompt=prompt
                )

    # def generate_response(question, llm_chain):
    response = llm_chain.run(sentence)
    return response

    # def get_text():
    #     # input_text = st.text_input("You: ", "", key="input")
    #     input_text = input("hi :")
    #     return input_text


# while 1 :
#     user_input = get_text()
#     response = generate_response(user_input, llm_chain)
# llm=HuggingFaceHub(repo_id="jondurbin/airoboros-l2-70b-gpt4-1.4.1", model_kwargs={"max_new_tokens":1200})

# input_text = "translate English to German: How old are you?"
# input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# outputs = model.generate(input_ids)
# print(tokenizer.decode(outputs[0]))
