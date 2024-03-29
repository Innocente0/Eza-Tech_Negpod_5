import cmd
from sys import exit

class EzaTechApp(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.logged_in = False
        self.username = None
        self.user_data = {}
