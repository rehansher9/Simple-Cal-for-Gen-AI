import streamlit as st

# Define functions for the calculator operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

# Streamlit app interface
def calculator_app():
    st.title("Simple Calculator")

    # Dropdown for operation selection
    operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Input fields for numbers
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")

    # Perform calculation based on the selected operation
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    # Display the result
    if st.button("Calculate"):
        st.write(f"The result is: {result}")

# Run the Streamlit app
if __name__ == "__main__":
    calculator_app()
