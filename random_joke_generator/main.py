import streamlit as st
import requests

# Custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #FF5733;
        text-align: center;
    }
    .joke-box {
        background-color: #FFD700;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        font-size: 20px;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #005F73;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://create-fast-api.vercel.app/")
        
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        
        else:
            return "Failed to fetch joke. Please try again later."
        
    except:
        return "Why did the chicken cross the road? \n\n To get to the other side!"

def main():
    st.markdown('<h1 class="main-title">😂 Random Joke Generator 😂</h1>', unsafe_allow_html=True)
    st.write("Click the button below to get a random joke")

    if st.button("Get a Joke 🎭"):
        joke = get_random_joke()
        st.markdown(f'<div class="joke-box">{joke}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
