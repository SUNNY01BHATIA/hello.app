class SimpleCalculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Define two numbers
num1 = 10
num2 = 5

# Perform calculations
addition_result = SimpleCalculator.add(num1, num2)
subtraction_result = SimpleCalculator.subtract(num1, num2)
multiplication_result = SimpleCalculator.multiply(num1, num2)
division_result = SimpleCalculator.divide(num1, num2)

# Display results
print(f"Addition: {num1} + {num2} = {addition_result}")
print(f"Subtraction: {num1} - {num2} = {subtraction_result}")
print(f"Multiplication: {num1} * {num2} = {multiplication_result}")
print(f"Division: {num1} / {num2} = {division_result}")
