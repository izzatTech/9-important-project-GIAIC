import streamlit as st
import time

st.title("Countdown Timer")

seconds = st.number_input("Enter time in seconds:", min_value=1, value=10)

if st.button("Start Countdown"):
    for i in range(seconds, 0, -1):
        st.write(f"Time remaining: {i} seconds")
        time.sleep(1)
    st.write("Time's up!")