import cmd

# Create a class that inherits from cmd.Cmd

class myCmd(cmd.Cmd):
    intro = "Welcome to my command line"
    prompt = "Console >>>>"
    
    def do_greet(self, line):
        print("Hey there, How can I help you?")
    
    def do_quit(self, line):
        return True
    def do_multiply(self, line):
        print(int(line.split()[0]) * int(line.split()[1]))
    def do_add(self, line):
        print(int(line.split()[0]) + int(line.split()[1]))

    
if __name__ == "__main__":
    myCmd().cmdloop()
