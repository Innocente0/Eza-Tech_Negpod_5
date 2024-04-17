import cmd
import os
from sys import exit

class EzaTechApp(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.logged_in = False
        self.username = None
        self.user_data = {}
        self.user_file = "registered_users.txt"
        self.farming_file = "farming_data.txt"

        if not os.path.exists(self.user_file):
            with open(self.user_file, "w"):
                pass

        if not os.path.exists(self.farming_file):
            with open(self.farming_file, "w"):
                pass

        self.load_registered_users()

    def print_menu(self):
        print("Eza-Tech Menu")
        print("============")
        print("1. Watch introduction video")
        print("2. Register")
        print("3. Login")
        print("3. Logout")
        print("4. Add farming data")
        print("5. Add livestock data")
        print("6. Access data")
        print("7. Exit")

    def do_menu(self, line):
        """Show the main menu options."""
        self.print_menu()

    def do_1(self, line):
        """Play the introduction video."""
        """Play the introduction video."""
        print("Playing introduction video...")
        print("Here's the link to our video: https://drive.google.com/file/d/12gctjL2aoHPJophjAaENpLG1R-sFYyhM/view?resourcekey")
        input("Press Enter to continue...")

    def do_2(self, line):
        """Register as a user."""
        self.register_user()

    def do_3(self, line):
        """Login as a user or Logout."""
        if not self.logged_in:
            self.login_user()
        else:
            self.logout_user()

    def do_4(self, line):
        """Add farming data."""
        self.add_farming_data()

    def do_5(self, line):
        """Add livestock data."""
        self.add_livestock_data()
    
    def do_6(self, line):
        """Access data."""
        self.access_data()

    def do_7(self, line):
        """Exit the application."""
        print("Exiting the application...")
        self.save_registered_users()
        exit(0)

    def login_user(self):
        """Login the current user."""
        username = self.get_user_input("Enter your username: ")
        if username in self.user_data:
            self.logged_in = True
            self.username = username
            print(f"Welcome, {self.username}!")
        else:
            print("User not found. Please register or try again.")

    def logout_user(self):
        """Logout the current user."""
        if self.logged_in:
            self.logged_in = False
            print(f"Goodbye, {self.username}!")
            self.username = None
        else:
            print("You are not logged in.")

    def add_farming_data(self):
        """Add farming data."""
        if self.logged_in:
            data = self.get_user_input("Enter farming data: ")
            with open(self.farming_file, "a") as file:
                file.write(f"{self.username}:{data}\n")
            print(f"Farming data added for user '{self.username}'")
        else:
            print("You need to be logged in to add farming data")

    def add_livestock_data(self):
        """Add Livestock Data."""
        if self.logged_in:
            data = self.get_user_input("Enter livestock data: ")
            # Add livestock data handling here if needed
            print("Livestock data added (not implemented)7")
        else:
            print("You need to be logged in to add livestock data")

    def access_data(self):
        """Access user data."""
        if self.logged_in:
            with open(self.farming_file, "r") as file:
                farming_data = file.readlines()
                user_farming_data = [line.strip() for line in farming_data if line.startswith(f"{self.username}:")]
                if user_farming_data:
                    print(f"Farming data for {self.username}:")
                    for data in user_farming_data:
                        print(data.split(":", 1)[1])
                else:
                    print("No farming data available.")
        else:
            print("You need to be logged in to access data.")

    def get_user_input(self, prompt):
        """Get user input and handle invalid input."""
        while True:
            user_input = input(prompt)
            if user_input:
                return user_input.strip()
            else:
                print("Input cannot be empty. Please try again.")

    def register_user(self):
        """Register a new user."""
        username = self.get_user_input("Enter a username: ")
        if username in self.user_data:
            print("This username already exists. Please choose another one")
        else:
            self.user_data[username] = {}
            print(f"User '{username}' registered successfully")

    def load_registered_users(self):
        """Load registered users from a file."""
        with open(self.user_file, "r") as file:
            for line in file:
                username = line.strip()
                self.user_data[username] = {}

    def save_registered_users(self):
        """Save registered users to a file."""
        with open(self.user_file, "w") as file:
            for username in self.user_data:
                file.write(f"{username}\n")

if __name__ == "__main__":
    app = EzaTechApp()
    app.print_menu()
    app.cmdloop()

