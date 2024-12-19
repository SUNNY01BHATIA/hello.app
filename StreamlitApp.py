def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Get user input
        choice = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            # Get numbers from user
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform the selected operation
            if choice == '1':
                print(f"The result of addition is: {num1 + num2}")
            elif choice == '2':
                print(f"The result of subtraction is: {num1 - num2}")
            elif choice == '3':
                print(f"The result of multiplication is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result of division is: {num1 / num2}")
                else:
                    print("Division by zero is not allowed.")
        else:
            print("Invalid choice! Please select a valid operation.")

        # Check if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()
