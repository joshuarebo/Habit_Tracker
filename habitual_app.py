from typing import List, Union, Dict, Any
from user import User
from storage_manager import StorageManager
from analytics_module import AnalyticsModule


class HabitualApp:
    def __init__(self):
        self.users: List[User] = []  # List to store user objects
        self.storage_manager: StorageManager = StorageManager()  # Storage manager object
        self.analytics_module: AnalyticsModule = AnalyticsModule()  # Analytics module object

    def create_user(self, username: str) -> None:
        """Create a new user."""
        user = User(username)
        self.users.append(user)

    def delete_user(self, username: str) -> None:
        """Delete an existing user."""
        if not isinstance(username, str):
            print("Error: Username must be a string.")
            return

        user = self.find_user(username)
        if user:
            self.users.remove(user)
            print("User deleted successfully.")
        else:
            print("User not found.")

    def find_user(self, username: str) -> Union[User, None]:
        """Find a user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def save_data(self) -> None:
        """Save application data to storage."""
        try:
            self.storage_manager.save_data(self.users)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        """Load application data from storage."""
        try:
            self.users = self.storage_manager.load_data()
        except Exception as e:
            print(f"Error loading data: {e}")

    def analyze_habits(self, username: str) -> Union[str, Dict[str, Any]]:
        """Analyze habits for a specific user."""
        user = self.find_user(username)
        if user:
            return self.analytics_module.analyze_habits(user)
        else:
            return "User not found."

    def display_menu(self) -> None:
        """Display the CLI menu."""
        print("Welcome to HABITUAL!")
        print("1. Create User")
        print("2. Delete User")
        print("3. Analyze Habits")
        print("4. Exit")

    def handle_input(self, choice: str) -> None:
        """Handle user input."""
        if choice == "1":
            username = input("Enter username: ")
            self.create_user(username)
            print("User created successfully.")
        elif choice == "2":
            username = input("Enter username to delete: ")
            self.delete_user(username)
        elif choice == "3":
            username = input("Enter username to analyze habits: ")
            analysis_result = self.analyze_habits(username)
            print(analysis_result)
        elif choice == "4":
            print("Exiting HABITUAL. Goodbye!")
            self.save_data()
            exit()
        else:
            print("Invalid choice. Please try again.")

    def run(self) -> None:
        """Run the CLI."""
        try:
            self.load_data()  # Load existing data
            while True:
                self.display_menu()
                choice = input("Enter your choice: ")
                self.handle_input(choice)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Test the HabitualApp class
    app = HabitualApp()
    app.run()

    # Test cases
    user1 = User("Alice")
    user2 = User("Bob")
    app.users.append(user1)
    app.users.append(user2)

    print("Users after creation:")
    for user in app.users:
        print(user.username)
