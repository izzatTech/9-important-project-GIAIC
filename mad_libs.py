import streamlit as st

# Title
st.title('Mad Libs Game')

# User inputs
name = st.text_input("Enter a name:")
place = st.text_input("Enter a place:")
animal = st.text_input("Enter an animal:")
adjective = st.text_input("Enter an adjective:")
verb = st.text_input("Enter a verb:")

# Mad Libs story
if st.button('Generate Story'):
    story = f"Once upon a time, {name} went to {place} and saw a {adjective} {animal}. It decided to {verb}!"
    st.write(story)