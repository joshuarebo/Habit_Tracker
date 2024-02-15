import time #Import time module
from habitual_app import HabitualApp

class CLIHandler:
    def __init__(self):
        self.app = HabitualApp()

    def display_menu(self):
        """Display the CLI menu."""
        print("Welcome to HABITUAL!")
        print("1. Create User")
        print("2. Delete User")
        print("3. Analyze Habits")
        print("4. Exit")

    def handle_input(self, choice):
        """Handle user input."""
        try:
            if choice == "1":
                username = input("Enter username: ")
                self.app.create_user(username)
                print("User created successfully.")
            elif choice == "2":
                username = input("Enter username to delete: ")
                self.app.delete_user(username)
                print("User deleted successfully.")
            elif choice == "3":
                username = input("Enter username to analyze habits: ")
                analysis_result = self.app.analyze_habits(username)
                if isinstance(analysis_result, dict):
                    print("Analysis Result:")
                    print(analysis_result)
                else:
                    print(analysis_result)
            elif choice == "4":
                print("Exiting HABITUAL. Goodbye!")
                self.app.save_data()  # Save data before exiting
                exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            time.sleep(5) # Add a ten second delay after printing each message

    def pick_predefined_habit(self):
        """Allow the user to pick a predefined habit."""
        print("Predefined Habits:")
        for index, habit in enumerate(self.predefined_habits, start=1):
            print(f"{index}. {habit}")
        try:
            choice = int(input("Choose a predefined habit (1-5): "))
            if 1 <= choice <= 5:
                self.app.create_habit(self.predefined_habits[choice - 1], "daily", 30)
                print(f"Habit '{self.predefined_habits[choice - 1]}' created successfully.")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        """Run the CLI."""
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            self.handle_input(choice)

if __name__ == "__main__":
    # Test the CLIHandler class
    cli_handler = CLIHandler()
    cli_handler.run()
