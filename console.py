
#!/usr/bin/python3
import cmd

class UserManagement(cmd.Cmd):
    """Simple crud Command fof managing users"""
    prompt = "Shell $"

    def __init__(self):
        super().__init__()
        self.users = {}  # A dictionaray to store users.

    def do_create(self, line):
        """Create a new user Syntax: 'create <digit> <name>'"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"User create - ID: {digit}, Name: {name}")
        else:
            print("Create a new user Syntax: 'create <digit> <name>'")


    def do_quit(self, line):
        return True
    def do_read(self, line):
        """Read and Sisplay all users"""
        print("List of users:")
        for digit, name in self.users.items():
            print(f"ID: {digit}, and Name: {name}")
    def do_update(self, line):
        """Update a user Syntax: 'update <digit> <name>'"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print(f"User updated - ID: {digit}, Name: {name}")
            else:
                print("User does not exist")
        else:
            print("Update a user Syntax: 'update <digit> <name>'")
    


if __name__ == '__main__':
    UserManagement().cmdloop()
