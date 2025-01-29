import json

class UserApp:
    def __init__(self):
        self.users = self.load_users()  # Load user data from file
        self.logged_in_user = None

    def load_users(self):
        """Load users from a JSON file."""
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty dictionary if the file doesn't exist or is invalid

    def save_users(self):
        """Save users to a JSON file."""
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=4)

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def register(self):
        print("\n--- Register ---")
        username = input("Enter a username: ").strip()
        if username in self.users:
            print("Username already exists. Please try a different one.")
            return

        password = input("Enter a password: ").strip()
        email = input("Enter your email: ").strip()
        age = input("Enter your age: ").strip()

        # Store user details in the dictionary
        self.users[username] = {
            "password": password,
            "email": email,
            "age": age
        }
        self.save_users()  # Save the updated users to the file
        print("User registered successfully!")

    def login(self):
        print("\n--- Login ---")
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        user = self.users.get(username)
        if user and user["password"] == password:
            self.logged_in_user = username
            print(f"Welcome, {username}!")
            self.user_menu()
        else:
            print("Invalid username or password.")

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. Show user details")
            print("2. Change password")
            print("3. Logout")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.show_user_details()
            elif choice == "2":
                self.change_password()
            elif choice == "3":
                print("Logged out successfully.")
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def show_user_details(self):
        if self.logged_in_user is None:
            print("No user is currently logged in.")
            return

        print("\n--- User Details ---")
        user = self.users.get(self.logged_in_user)
        if user:
            print(f"Username: {self.logged_in_user}")
            print(f"Email: {user['email']}")
            print(f"Age: {user['age']}")
        else:
            print("User details could not be found.")

    def change_password(self):
        print("\n--- Change Password ---")
        current_password = input("Enter your current password: ").strip()

        user = self.users.get(self.logged_in_user)
        if user and user["password"] == current_password:
            new_password = input("Enter a new password: ").strip()
            user["password"] = new_password
            self.save_users()  # Save the updated password to the file
            print("Password changed successfully!")
        else:
            print("Incorrect current password. Please try again.")


# Run the application
if __name__ == "__main__":
    app = UserApp()
    app.main_menu()
