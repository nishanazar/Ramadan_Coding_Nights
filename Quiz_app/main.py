import streamlit as st
import random
import time

# 🎨 Add Custom Styling for Better UI
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
    }
    .stRadio > label {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎯 Python Quiz Game")

# 📝 Questions List
questions = [
    {
    "question": "What is the extension of Python files?", 
     "options": [".java", ".py", ".cpp", ".html"], 
     "answer": ".py"
     },

    {
    "question": "Which function is used to display output in Python?",
    "options": ["echo()", "display()", "print()", "show()"],
    "answer": "print()"
    },
    {
    "question": "Which keyword is used to define a function in Python?", 
    "options": ["func", "def", "define", "lambda"], 
    "answer": "def"
    },
    {
    "question": "What is the output of: print(type([]))?", 
     "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
     "answer": "<class 'list'>"
     },
    {
    "question": "Which of the following data types is immutable in Python?", 
    "options": ["list", "set", "tuple", "dictionary"], 
    "answer": "tuple"
    },
    {
    "question": "Which built-in function is used to get the length of a list in Python?", 
    "options": ["count()", "size()", "length()", "len()"],
    "answer": "len()"
    },
    {
    "question": "Which of the following is NOT a valid variable name in Python?", 
    "options": ["my_variable", "2variable", "_private", "var_name"], 
    "answer": "2variable"
    },
    {
    "question": "Which of these statements is used to exit a loop in Python?", 
    "options": ["exit", "return", "break", "stop"], 
    "answer": "break"
    },
    {
    "question": "How do you take input from a user in Python?", 
    "options": ["input()", "scan()", "read()", "get()"], 
    "answer": "input()"},
    {
    "question": "Which data type is used to store text in Python?",
      "options": ["int", "str", "float", "bool"], 
      "answer": "str"
      },
]

# 🎯 Initialize Session State Variables
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = 0  
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = 0    

# 🏆 Display Score & Stats
st.markdown(f"**🏆 Score: {st.session_state.score}**")
st.markdown(f"✅ Correct Answers: {st.session_state.correct_answers}")
st.markdown(f"❌ Wrong Answers: {st.session_state.wrong_answers}")


# 🎯 Display Current Question
if st.session_state.question_index < len(questions):
    question = questions[st.session_state.question_index]
    st.subheader(f"{st.session_state.question_index + 1}: {question['question']}")

    selected_option = st.radio("Select an option", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.success("✅ Correct Answer!")
            st.session_state.score += 1
            st.session_state.correct_answers += 1  
        else:
            st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
            st.session_state.wrong_answers += 1  
        time.sleep(2)

# 🔄 Next Question Button
if st.button("Next Question"):
    st.session_state.question_index += 1  

    # 🎉 If all questions completed, restart quiz
    if st.session_state.question_index >= len(questions):
        st.success("🎉 Quiz Completed! Restarting...")
        time.sleep(2)
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.correct_answers = 0  
        st.session_state.wrong_answers = 0    

    st.rerun()
