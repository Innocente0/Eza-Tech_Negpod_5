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
        print("Registering user...")
        # Here, you can add the code to handle the registration process.
        self.register_user()
        input("Press Enter to continue...")

    def do_3(self, line):
        """Login and access the application."""
        if not self.logged_in:
            print("Logging user in...")
            # Here, you can add the code to handle the login process.
            self.login_user()
            self.do_menu(None)
        else:
            print("You are already logged in!")

    def do_4(self, line):
        """Exit the application."""
        print("Exiting the application...")
        exit(0)

    def do_add_farming_data(self, line):
        """Add farming data."""
        if self.logged_in:
            print("Adding farming data...")
            # Here, you can add the code to handle data input for farming.
        else:
            print("Please log in to access this feature.")

    def do_add_livestock_data(self, line):
        """Add livestock data."""
        if self.logged_in:
            print("Adding livestock data...")
            # Here, you can add the code to handle data input for livestock.
        else:
            print("Please log in to access this feature.")

    def do_access_data(self, line):
        """Access data."""
        if self.logged_in:
            print("Accessing data...")
            # Here, you can add the code to handle data access for logged-in users.
        else:
            print("Please log in to access this feature.")

    def login_user(self):
        self.logged_in = True

    def register_user(self):
        self.logged_in = True

if __name__ == "__main__":
    app = EzaTechApp()
    app.print_menu()
    app.cmdloop()
This is the code for the entire prototype

Innocente Niwemwana, 14:40
Hi Victoria

You, 14:44
Hi

Innocente Niwemwana, 14:55
Sorry for the delay
what I can do, should I create the repo or ??

You, 14:56
Yes
And make it private

Liliane Umwanankabandi, 15:05
heyy guys why cant  we work together if everyone is available
i think it can be good

You, 15:06
The issue is that everyone is not onlibe

Innocente Niwemwana, 15:11
@Liliane Umwanankabandi yes

Innocente Niwemwana, 15:28
Eza-Tech_Negpod_5
is this name ok, for the repo

You, 15:32
Yes

Innocente Niwemwana, 15:37
Can you send me your github username
I am trying to send invite using email but I can find  each one of you.

Sekata Moss Aimelyse Mfuranziza, 15:38
mfuranziza

You, 15:39
Pam-Pam29

Liliane Umwanankabandi, 15:41
Umwanankabandi-liliane

You, 8 min

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

