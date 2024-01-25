#!/usr/bin/python3
"""
Module for console
"""

import cmd

class HBNBCommand(cmd.Cmd):
     """
    HBNBCommand console class
    """

    prompt = "(hbnb)"

    def do_quit(self , args):
        """
        Module for console
        """
        return True
    def do_EOF(self, args):
        """
         EOF (Ctrl+D) signal to exit the program.
         """
         print()
         return True


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
