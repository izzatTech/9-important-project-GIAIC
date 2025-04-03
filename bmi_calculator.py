import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Streamlit UI
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.1, step=0.01)

# Ensure that the inputs are valid (positive values)
if weight > 0 and height > 0:
    # Calculate BMI when button is pressed
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")

        # BMI categories
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
else:
    st.warning("Please enter valid weight and height values.")