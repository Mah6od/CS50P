# Prompt the user for a mathematical expression
expression = input("Expression: ").strip()

try:
    # Use the eval() function to evaluate the expression
    result = float(eval(expression))

    # Print the result
    print("Result:", result)
except Exception as e:
    # Handle any potential errors, such as invalid expressions
    print("Error:", e)