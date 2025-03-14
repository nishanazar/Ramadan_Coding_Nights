import streamlit as st

st.title("Simple Streamlit App")
user_input = st.text_input("Enter your text:")

if st.button("Show Text"):
    st.write(f"Your entered: {user_input}")


# create fastapi file 