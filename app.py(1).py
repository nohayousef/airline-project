app.py
import streamlit as st

# Title and Headers
st.title("Welcome to airline Data Set")
st.header("The dataset contains 15,000 entries and 14 columns. Here's a summary of the columns")

# Column descriptions
st.subheader("1. Gender: Gender of the passengers (Female, Male)")
st.subheader("2. Customer Type: The customer type (Loyal customer, disloyal customer)")
st.subheader("3. Age: The actual age of the passengers")
st.subheader("4. Type of Travel: Purpose of the flight of the passengers (Personal Travel, Business Travel)")
st.subheader("5. Class: Travel class in the plane of the passengers (Business, Eco, Eco Plus).")

# About the dataset
st.title("About Data Set")
st.text("""
This dataset contains an airline passenger satisfaction survey. What factors are highly correlated to a satisfied (or dissatisfied) passenger? Can you predict passenger satisfaction?

""")

# Example of code block
st.code("int y = 3;", language='cpp')

# Markdown text with HTML styling
st.markdown("#### Markdown cell")
st.markdown("<span style='color:blue; font-size:30px;'>Span Normal Text</span>", unsafe_allow_html=True)
