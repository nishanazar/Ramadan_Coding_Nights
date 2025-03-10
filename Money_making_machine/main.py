import streamlit as st
import random
import time
import requests


st.title("Money Making Machine")

def generter_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generter_money()
    st.success(f"you made ${amount}!")


def fetch_side_hustle():
    try:
        responsive = requests.get("http://127.0.0.1:8000/side_hustles")
        if responsive.status_code == 200:
            hustles =  responsive.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")

    except:
        return("somthing went wrong!")
    
st.subheader("Side Hustle Ideas")

if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)
