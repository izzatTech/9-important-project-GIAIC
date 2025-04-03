# Save this as app.py
import streamlit as st

# Title of the website
st.title("Welcome to My Python Website!")

# Simple message
st.write("This is a basic website created with Streamlit!")

# Button functionality
if st.button("Click Me"):
    st.write("You clicked the button!")