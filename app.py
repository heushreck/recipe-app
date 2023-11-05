import random
import string
import streamlit as st

if 'ingredeant_inputs' not in st.session_state:
    st.session_state.ingredeant_inputs= []
    st.session_state.ingredeant_inputs.append(random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

def add_new_ingredeant(input_key):
    position = st.session_state.ingredeant_inputs.index(input_key)
    if position == len(st.session_state.ingredeant_inputs)-1:
        st.session_state.ingredeant_inputs.append(random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

st.header("What's your recipe?")
st.subheader("Name")
name = st.text_input("Please write down your recipe name")
st.subheader("Ingrediants")
ingrediants = []
for input_key in st.session_state.ingredeant_inputs:
    input_value = st.text_input(
        "Please write down your ingredeants", 
        key=input_key, 
        on_change=add_new_ingredeant, 
        kwargs={'input_key': input_key},
    )
    ingrediants.append(input_value)

st.write(ingrediants)
