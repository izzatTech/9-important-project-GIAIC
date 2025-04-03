import streamlit as st

# Title
st.title('Guess the Number (User Version)')

# Instructions
st.write("Think of a number between 1 and 100, and I'll try to guess it!")

# Variables
low, high = 1, 100
attempts = 0

# User input
user_feedback = st.radio("Is the number:", ("Higher", "Lower", "Correct"))

# Game loop
if user_feedback == "Higher":
    low = (low + high) // 2 + 1
    attempts += 1
elif user_feedback == "Lower":
    high = (low + high) // 2 - 1
    attempts += 1
elif user_feedback == "Correct":
    attempts += 1
    st.success(f"I guessed your number in {attempts} attempts!")