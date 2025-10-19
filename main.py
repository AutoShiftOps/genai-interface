import streamlit as st
import langchain_helper
import pandas as pd

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cusine", ("indian", "Italian", "Mexican", "Arabian"))

if cuisine:
    response = langchain_helper.generate_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip()
    print(response['menu_items'])
    st.write("**Menu Items**")
    st.write(menu_items)