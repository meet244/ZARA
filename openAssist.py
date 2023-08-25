import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv
load_dotenv()


def response(sentence):


    template = """<|prompter|>{question}<|endoftext|><|assistant|>"""
    
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm=HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens":1200})
    # llm=HuggingFaceHub(repo_id="jondurbin/airoboros-l2-70b-gpt4-1.4.1", model_kwargs={"max_new_tokens":1200})

    llm_chain=LLMChain(
        llm=llm,
        prompt=prompt
    )

    response = llm_chain.run(sentence)
    # print(response)
    return response



# def selfTry(sentence):

#     template = """<|prompter|>you are my personal virtual assistant named 'ZARA'. {question}<|endoftext|><|assistant|>"""
    
#     prompt = PromptTemplate(template=template, input_variables=["question"])

#     llm=HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens":1200})
#     # llm=HuggingFaceHub(repo_id="jondurbin/airoboros-l2-70b-gpt4-1.4.1", model_kwargs={"max_new_tokens":1200})

#     llm_chain=LLMChain(
#         llm=llm,
#         prompt=prompt
#     )

#     response = llm_chain.run(sentence)
#     response = llm_chain.run(sentence)
#     # print(response)
#     return response

