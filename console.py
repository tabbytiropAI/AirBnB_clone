#!/usr/bin/python3
"""Command interpreter for the AirBnB project"""

import cmd
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to the JSON file, and print the ID"""
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
        """Show string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + "." + args[1]
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + "." + args[1]
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        obj_dict = storage.all()

        if not arg:
            print([str(obj_dict[obj]) for obj in obj_dict])
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_instances = [str(obj_dict[obj]) for obj in obj_dict if obj.startswith(arg + ".")]
            if not class_instances:
                print("** no instance found **")
            else:
                print(class_instances)

    def do_update(self, arg):
        """Update an instance's attributes"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + "." + args[1]

        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        try:
            setattr(obj_dict[key], args[2], eval(args[3]))
            storage.save()
        except AttributeError:
            print("** attribute doesn't exist **")

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handle end of file (Ctrl-D)"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

