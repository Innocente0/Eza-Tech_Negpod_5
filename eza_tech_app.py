import cmd
from sys import exit

class EzaTechApp(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.logged_in = False
        self.username = None
        self.user_data = {}

    def print_menu(self):
        print("Eza-Tech Menu")
        print("============")
        print("1. Watch introduction video")
        print("2. Register")
        print("3. Login")
        print("4. Logout")
        print("5. Add farming data")
        print("6. Add livestock data")
        print("7. Access data")
        print("8. Exit")

    def do_menu(self, line):
        """Show the main menu options."""
        self.print_menu()

    def do_1(self, line):
        """Play the introduction video."""
        print("Playing introduction video...")
        input("Press Enter to continue...")

    def do_2(self, line):
        """Register as a user."""
        self.register_user()

    def do_3(self, line):
        """Login as a user."""
        self.login_user()

    def do_4(self, line):
        """Logout as a user."""
        self.logout_user()

    def do_5(self, line):
        """Add farming data."""
        self.add_farming_data()

    def do_6(self, line):
        """Add livestock data."""
        self.add_livestock_data()
    
    def do_7(self, line):
        """Access data."""
        self.access_data()

    def do_8(self, line):
        """Exit the application."""
        print("Exiting the application...")
        exit(0)

    def login_user(self, prompt):
        """Login the current user."""
        print("Logged in")

    def add_livestock_data(self, prompt):
        """Add Livestock Data."""
        print("Coming Soon")   
    
    def access_data(self, prompt):
        """Get Data"""
        print("Coming Soon")
    
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
            self.logged_in = True
            self.username = username
            print(f"User '{self.username}' registered successfully")
    def logout_user(self):
        """Logout the current user."""
        if self.logged_in:
            self.logged_in = False
            self.username = None
            print(f"User '{self.username}' logged out successfully")
        else:
            print("You are not logged in.")
    def add_farming_data(self):
        """Add farming data."""
        if self.logged_in:
            data = self.get_user_input("Enter farming data: ")
            self.user_data[self.username]["farming"] = data
            print(f"Farming data added for user '{self.username}'")
        else:
            print("You need to be logged in to add farming data")

if __name__ == "__main__":
    app = EzaTechApp()
    app.print_menu()
    app.cmdloop()

