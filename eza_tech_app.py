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

