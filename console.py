#!/usr/bin/python3
"""
module contains HBNBCommand
"""
import cmd
import re
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
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
                  "Review": Review, "User": User}

    def precmd(self, line):
        """ doc"""
        if not line:
            pass
        elif re.match(r'^\w+\.\w+\(\)$', line):
            line = line.replace(".", " ")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.split()[1] + " " + line.split()[0]
            return line
        elif re.match(r'(\w+)\.(\w+)\((\'[^\']*\'|"[^"]*")\)', line):
            matches = re.match(r'(\w+)\.(\w+)\((\'[^\']*\'|"[^"]*")\)', line)
            string1 = matches.group(1)
            string2 = matches.group(2)
            string3 = matches.group(3)
            if string3.startswith("'") or string3.startswith('"'):
                string3 = string3[1:-1]
            line = (f"{string2} {string1} {string3}")
            return line
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
        args = line.split()
        if len(args) >= 2:
            if args[0] in HBNBCommand.class_dict:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all().get(key))
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            print("** class name missing **")

    def do_destroy(self, line):
        """ remove an instance base on classname"""
        args = line.split()
        if len(args) >= 2:
            if args[0] in HBNBCommand.class_dict:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.destroy(key)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            print("** class name missing **")

    def do_all(self, line):
        """ returns all instances in storage"""
        args = line.split()
        obj_list = []
        if len(args) >= 1:
            if args[0] in HBNBCommand.class_dict:
                for k, v in storage.all().items():
                    if k.startswith(args[0]):
                        obj_list.append(str(v))
                        print(obj_list)
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            for v in storage.all().values():
                obj_list.append(str(v))
                print(obj_list)

    def do_update(self, line):
        """  update the attribute of an object
            ex:
            update BaseModel 89398838 email "888@.com"
        """
        args = line.split()
        if len(args) >= 4:
            if args[0] in HBNBCommand.class_dict:
                obj_id = args[0] + "." + args[1]
                if obj_id in storage.all():
                    setattr(storage.all()[obj_id], args[2],
                            str(args[3].strip('"')))
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 3:
            if args[0] in HBNBCommand.class_dict:
                obj_id = args[0] + "." + args[1]
                if obj_id in storage.all():
                    print("** value missing **")
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 2:
            if args[0] in HBNBCommand.class_dict:
                obj_id = args[0] + "." + args[1]
                if obj_id in storage.all():
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.class_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            print("** class name missing **")

    def do_count(self, line):
        """
        counting number of instances
        of a class
        """
        count = 0
        for k in storage.all().keys():
            if line == k.split(".")[0]:
                count += 1
        print(count)

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

    def help_destroy(self):
        """ doc"""
        print("Destroy command to remove an instance")

    def help_all(self):
        """ doc"""
        print("All instances of object class")

    def help_update(self):
        """ doc"""
        print("Update an instance of class")

    def help_count(self):
        """ doc"""
        print("Count number of class instance(s)")

    def help_quit(self):
        """ help dock for quit """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """ terminate command ctrl+d """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
