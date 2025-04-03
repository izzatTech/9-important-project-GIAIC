import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_special_chars):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title('Password Generator')

# Input for password length
length = st.slider('Select password length:', min_value=8, max_value=20, value=12)

# Checkbox for including special characters
use_special_chars = st.checkbox('Include special characters')

# Generate button
if st.button('Generate Password'):
    password = generate_password(length, use_special_chars)
    st.write(f"Generated Password: {password}")