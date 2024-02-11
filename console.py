#!/usr/bin/python3
"""This module serves as the entry point
 for the command interpreter of the HBNB project,
 providing a command-line interface to interact
 with the application"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for command interpreter inherit
    cmd module providing a command-line interface to
    interact with the application.
    to include creating, showing, updating, and
    destroying instances of different classes
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print([str(obj) for key, obj in objects.items() if arg in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()

