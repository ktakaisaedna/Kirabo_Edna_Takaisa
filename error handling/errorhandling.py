def get_number(prompt):
    """Get a valid number from user input with error handling."""
    while True:
        try:
            user_input = input(prompt)
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'q']:
                return None
            # Convert to float to handle both integers and decimals
            number = float(user_input)
            return number
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            return None

def divide_numbers():
    """Main function to handle division with error checking."""
    print("Division Calculator")
    print("Enter 'quit', 'exit', or 'q' to exit the program")
    print("-" * 40)
    
    while True:
        # Get first number
        print("\nEnter two numbers to divide:")
        num1 = get_number("First number (dividend): ")
        if num1 is None:
            print("Goodbye!")
            break
            
        # Get second number
        num2 = get_number("Second number (divisor): ")
        if num2 is None:
            print("Goodbye!")
            break
            
        # Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero! Please enter a non-zero divisor.")
            continue
            
        # Perform division
        try:
            result = num1 / num2
            print(f"\nResult: {num1} ÷ {num2} = {result}")
            
            # Ask if user wants to continue
            while True:
                try:
                    continue_choice = input("\nDo you want to perform another division? (y/n): ").lower()
                    if continue_choice in ['y', 'yes']:
                        break
                    elif continue_choice in ['n', 'no']:
                        print("Goodbye!")
                        return
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                except KeyboardInterrupt:
                    print("\nProgram interrupted by user. Goodbye!")
                    return
                    
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

# Run the program
if __name__ == "__main__":
    divide_numbers()