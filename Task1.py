# pythonv
# Addition
# Subtraction
# Multiplication
# Division
# Step 1: Take two numbers as input

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Step 3: Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

