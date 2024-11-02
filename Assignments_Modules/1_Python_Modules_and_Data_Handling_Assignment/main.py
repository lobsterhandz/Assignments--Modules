# main.py
import mood_responses
import menu

def main():
    while True:
        try:
            print(menu.show_menu())
            choice = input("Enter your choice (1, 2, or 3): ")
            
            if choice == '1':
                mood = input("How are you feeling today? ")
                response = mood_responses.mood_response(mood)
                print(response)
            elif choice == '2':
                new_mood = input("Enter the mood you want to add: ")
                new_response = input(f"Enter the response for mood '{new_mood}': ")
                confirmation = mood_responses.add_mood(new_mood, new_response)
                print(confirmation)
            elif choice == '3':
                print("Goodbye! Have a great day!")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
