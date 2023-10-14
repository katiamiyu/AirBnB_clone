#!/usr/bin/python3
"""
module contains HBNBCommand
"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class use to run interactive terminal for
    entry into Airbnbclone app
    attributes:
        prompt (str): focus display string
    """
    prompt = "(hbnb) "
    command_list = ["create", "show", "all", "update",
                    "show", "destroy"]
    class_dict = {"BaseModel": BaseModel, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def precmd(self, line):
        """ doc"""
        if not line:
            pass
        else:
            if line in HBNBCommand.command_list:
                return line
        return line

    def do_create(self, line):
        """ create new instance"""
        if not line:
            print("** class name missing **")
        elif line.strip() in HBNBCommand.class_dict:
            obj = HBNBCommand.class_dict[line]()
            storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ shows an instance"""
        if line:
            args = line.split()
            if len(args) >= 2:
                if args[0] in HBNBCommand.class_dict:
                    obj_id = args[0] + "." + args[1]
                    if obj_id in storage.all():
                        obj = storage.all().get(obj_id)
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def do_quit(self, line):
        """ exits the app """
        return True

    def emptyline(self):
        pass

    def help_create(self):
        """ doc"""
        print("Create command to create a new instance")

    def help_show(self):
        """ doc"""
        print("Show command to display an instance")

    def help_all(self):
        """ doc"""
        print("All instances of object class")

    def help_update(self):
        """ doc"""
        print("Update an instance of class")

    def help_quit(self):
        """ help dock for quit """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """ terminate command ctrl+d """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
