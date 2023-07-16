#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models
import shlex
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defined the HolbertonBnB command interpreter.

    Attributes:
        prompt: The command prompt.
        """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """to exit the program."""
        return True

    def do_EOF(self, arg):
        """to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing receiving an empty line."""
        pass

    def do_create(self, args):
        '''
        Create a new instance of BaseModel and saves it
        to the JSON file.
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            newInstance = eval(args[0])()
            newInstance.save()
            print(newInstance.id)

        except:
            print("** class doesn't exist **")

