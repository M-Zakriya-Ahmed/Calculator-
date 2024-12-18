import streamlit as st

# Title of the app
st.title('Simple Calculator')

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Dropdown for selecting operation
operation = st.selectbox("Choose an operation", ['+', '-', '*', '/'])

# Perform the calculation based on the selected operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write(f"The result is: {result}")
