# main.py

# Import TextUtils class from text_utils module with an alias
from text_utils import TextUtils as tu

def main():
    while True:
        # Display a menu to the user
        print("\n--- Text Utility Application ---")
        print("1. Reverse a String")
        print("2. Capitalize a String")
        print("3. Remove Whitespace from a String")
        print("4. Quit")

        # Get user's choice
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        # Handle user's choice
        if choice == 1:
            user_input = input("Enter the string to reverse: ")
            try:
                result = tu.reverse_string(user_input)
                print(f"Reversed String: '{result}'")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 2:
            user_input = input("Enter the string to capitalize: ")
            try:
                result = tu.capitalize_string(user_input)
                print(f"Capitalized String: '{result}'")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            user_input = input("Enter the string to remove whitespace from: ")
            try:
                result = tu.remove_whitespace(user_input)
                print(f"String without Whitespace: '{result}'")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 4:
            print("Exiting the Text Utility Application. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
