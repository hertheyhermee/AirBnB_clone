#!/usr/bin/python3
'''
This module contains the console for AirBnB.
'''
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
    Description:
        Contains the entry point of the command interpreter.
    '''

    prompt = "(hbnb) "

    def do_quit(self, args):
        '''
        Description:
            Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        '''
        Description:
            Exits after receiving the EOF command.
        '''
        print()
        return True

    def do_create(self, args):
        '''
        Description:
            Create a new instance of class BaseModel and saves it
            to the JSON file.
        '''
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''
        Description:
            Display string representation of an instance based on
            the class name and id given as arguments.
        '''
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = FileStorage().all()
        try:
            obj = obj_dict[args[0] + "." + args[1]]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        '''
        Description:
            Deletes an instance based on class name and id.
        '''
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = FileStorage().all()
        try:
            key = args[0] + "." + args[1]
            del obj_dict[key]
            FileStorage().save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        '''
        Description:
            Prints all string representation of all instances.
        '''
        obj_list = []
        obj_dict = FileStorage().all()
        if args:
            try:
                objects = obj_dict[args]
                obj_list = [str(obj) for obj in objects.values()]
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            obj_list = [str(obj) for obj in obj_dict.values()]
        print(obj_list)

    def do_update(self, args):
        '''
        Description:
            Update an instance based on the class name and id.
        '''
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj_dict = FileStorage().all()
        try:
            key = args[0] + "." + args[1]
            obj = obj_dict[key]
            attr_name = args[2]
            attr_value = args[3]
            if hasattr(obj, attr_name):
                attr_value = type(getattr(obj, attr_name))(attr_value)
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        '''
        Description:
            Do nothing when an empty line is passed.
        '''
        pass

    def do_count(self, args):
        '''
        Description:
            Returns the number of instances.
        '''
        obj_dict = FileStorage().all()
        if args:
            try:
                objects = obj_dict[args]
                print(len(objects))
            except KeyError:
                print("** class doesn't exist **")
        else:
            print(len(obj_dict))

    def default(self, args):
        '''
        Description:
            Points to the required method in the dictionary based on
            the commands given as a key.
        '''
        functions = {
            "all": self.do_all,
            "update": self.do_update,
            "show": self.do_show,
            "count": self.do_count,
            "destroy": self.do_destroy
        }
        args = (
            args.replace("(", ".").replace(")", ".").replace('"', "")
            .replace(",", "").split(".")
        )

        try:
            cmd_arg = args[0] + " " + args[1]
            func = functions[args[2]]
            func(cmd_arg)
        except IndexError:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    '''
        Entry point for the loop.
    '''
    HBNBCommand().cmdloop()
