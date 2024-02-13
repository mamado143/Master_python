#!/usr/bin/python3
import cmd
import json

class UserManagement(cmd.Cmd):
    """Simple CRUD Command for managing users"""
    prompt = "Shell $"

    def __init__(self):
        super().__init__()
        self.users = self.load_from_file()  # Load data from file
        if not self.users:
            self.users = {}

    def do_create(self, line):
        """Create a new user Syntax: 'create <digit> <name>'"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"User created - ID: {digit}, Name: {name}")
            self.save_to_file()  # Save changes to file
        else:
            print("Create a new user Syntax: 'create <digit> <name>'")

    def do_read(self, line):
        """Read and Display all users"""
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
                self.save_to_file()  # Save changes to file
            else:
                print("User does not exist")
        else:
            print("Update a user Syntax: 'update <digit> <name>'")

    def do_destroy(self, line):
        """Delete a User by ID Syntax: 'destroy <digit>'"""
        if line in self.users:
            del self.users[line]
            print(f"User deleted - ID: {line}")
            self.save_to_file()  # Save changes to file
        else:
            print(f"No user found with ID {line}")

    def do_quit(self, line):
        """Quit the shell"""
        return True

    def save_to_file(self):
        """Save data to file"""
        with open("user_data.json", "w") as json_file:
            json.dump(self.users, json_file)

    def load_from_file(self):
        """Load data from file"""
        try:
            with open("user_data.json", "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return None

if __name__ == '__main__':
    UserManagement().cmdloop()
