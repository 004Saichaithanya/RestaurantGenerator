# langchain_model.py

import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_mistralai import ChatMistralAI

# Load API key from .env
load_dotenv()

# Initialize LLM
llm = ChatMistralAI(model="mistral-tiny")


def generate_restaurant_details(cuisine):
    # Prompt for restaurant name
    prompt_res_name = PromptTemplate(
        input_variables=["cuisine"],
        template = "Suggest a unique and fancy name for a new {cuisine} restaurant opening in the USA. The name should appeal to people of all backgrounds. Return only the restaurant name and a short, catchy brand quote. No explanation.",
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_res_name, output_key="restaurant_name")

    # Prompt for menu items
    prompt_menu_name = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest a well-structured menu for a restaurant named "{restaurant_name}". 
                    Organize the items under clear sections such as:
                    - Appetizers
                    - Main Course
                    - Desserts
                    Include only popular and appealing dishes. Return the menu items in each section as a comma-separated list under appropriate headings.""",
    )
    menu_chain = LLMChain(llm=llm, prompt=prompt_menu_name, output_key="menu")

    # Chain both together
    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu"],
    )

    return chain({"cuisine": cuisine})

