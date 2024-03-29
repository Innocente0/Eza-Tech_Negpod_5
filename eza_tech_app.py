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

