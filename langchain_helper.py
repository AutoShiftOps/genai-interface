from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
import os
import streamlit as st


# Access the secret key using st.secrets
# Set it as an environment variable so LangChain can pick it up automatically
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = OpenAI(temperature=0.7)

def generate_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a single fancy name for this."
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return the data into categories with prices as string format"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain.invoke({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    print(generate_name_and_items("Indian"))