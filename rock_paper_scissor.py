import streamlit as st
import random

# Title
st.title('Rock, Paper, Scissors Game')

# User input
user_choice = st.selectbox('Choose your option:', ['Rock', 'Paper', 'Scissors'])

# Computer choice
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

# Display choices
st.write(f'You chose: {user_choice}')
st.write(f'The computer chose: {computer_choice}')

# Determine winner
if user_choice == computer_choice:
    result = 'It\'s a tie!'
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
     (user_choice == 'Paper' and computer_choice == 'Rock') or \
     (user_choice == 'Scissors' and computer_choice == 'Paper'):
    result = 'You win!'
else:
    result = 'You lose!'

# Display result
st.write(result)