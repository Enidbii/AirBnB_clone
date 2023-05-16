#!/usr/bin/python3
""" console module """
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter """
    prompt = '(hbnb) '

    def do_prompt(self, line):
        self.prompt = line

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return False

    def help_quit(self):
        """ handles two arguments """
        print('\n'.join(["Quit command to exit the program"]))

    def do_create(self, line):
        if line:
            try:
                obj = global().get(line, 
                obj.save()
                print(obj.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
