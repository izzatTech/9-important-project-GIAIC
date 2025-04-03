import streamlit as st
import random

# Title
st.title('Guess the Number Game')

# Generate random number
number = random.randint(1, 100)

# User input
guess = st.number_input('Guess a number between 1 and 100', min_value=1, max_value=100)

# Check guess
if st.button('Check'):
    if guess == number:
        st.success(f"Congratulations! {guess} is the correct number!")
    elif guess < number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")