from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import logging
from celery.utils.log import get_task_logger
from .worker import app
load_dotenv()
api = os.environ['LLama_API']

celery_log = get_task_logger(__name__)



@app.task(name="app.classify_article" , retry_kwargs={'max_retries': 5})
def classify_article(article):
    llama = LlamaAPI(api_token=api)

    model = ChatLlamaAPI(client=llama)

    prompt_template = """
    Act as an expert in text classification.
    I want you to take a text as an input and classify it into one of the following categories: Terrorism/protest/political/riot, Positive/uplifting, Natural Disasters, or Others.
    Main Instructions:
    - your response should not increase than one word in which category the given text belong to .
    - Please provide a response indicating the category without any kind explanation.

    here is the text
    {text} 

    """
    Prompt = PromptTemplate(template=prompt_template, input_variables=['text'])
    chain = LLMChain(llm=model, prompt=Prompt)
    
    category = chain.invoke(article['content'])['text']
    return category
