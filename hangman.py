import streamlit as st
import random

st.title("Hangman Game")

# List of words for the game
words = ["python", "hangman", "programming", "streamlit", "developer"]

# Select a random word
word = random.choice(words).lower()
guessed_letters = []
attempts = 6  # Number of allowed wrong guesses

# Display word with blanks for unguessed letters
display_word = ""
for letter in word:
    if letter in guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.write(display_word)

# User input for guessing a letter
letter = st.text_input('Guess a letter:', '').lower()

if st.button('Submit'):
    if len(letter) == 1 and letter.isalpha():
        if letter in guessed_letters:
            st.warning("You already guessed that letter!")
        elif letter in word:
            st.success("Correct guess!")
            guessed_letters.append(letter)
        else:
            st.error("Wrong guess!")
            attempts -= 1
            guessed_letters.append(letter)
    else:
        st.warning("Please enter a single letter.")

# Check win/lose conditions
if all(letter in guessed_letters for letter in word):
    st.balloons()
    st.success("Congratulations! You won!")
elif attempts <= 0:
    st.error(f"Game over! The word was: {word}")

# Display remaining attempts
st.write(f"Attempts left: {attempts}")