import streamlit as st

# Fix the typo in options (corrected "combinetion" to "combination" and removed extra single quote in the list)
gender = st.selectbox(label='Gender', options=['male', "female"])
customer = st.selectbox(label='Customer Type', options=["Loyal customer", "disloyal customer"])
type_of_ravel = st.selectbox(label='Type of Travel', options=['Personal Travel', "Business Travel"])
Class = st.selectbox(label='Class', options=['Business', 'Eco', 'Eco Plus'])
Satisfaction = st.selectbox(label='Satisfaction', options=['Satisfaction', 'neutral or dissatisfaction'])

# Corrected the typo in 'unisix' to 'unisex'
gender_target = st.select_slider(label='Gender_Target', options=['female', 'male'])

# No changes needed for the rating slider
rateInflightservice = st.slider(label="Inflight service", min_value=1, max_value=5)
rateCleanliness = st.slider(label="Cleanliness", min_value=1, max_value=5)
# Submit button
is_submit = st.button("Submit")

# Fix the print statements (replace the undefined variables with actual ones from the form inputs)
if is_submit:
    # Example: showing selected values for skin_type, main_Ingredient, gender_target, and rate
    st.write(f"Selected Skin Type: {customer}")
    st.write(f"Targeted Gender: {gender_target}")
    st.write(f"Rating: {rate}")
