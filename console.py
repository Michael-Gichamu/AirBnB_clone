#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Implements the console for AirBnB clone web application.
    """
    prompt = '(hbnb) '

    def do_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_quit(self, argv):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_create(self, argv):
        args = argv.split()
        if args == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, argv):
        args = argv.split()
        if args == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = self.get_instance_key(args)
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[instance_key]
                print(instance)

    def do_all(self, argv):
        args = argv.split()
        if args == "":
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class deosn't exist **")
            return

        obj = storage.all()
        list_instances = []

        for key in obj.keys():
            instance = obj[key]
            list_instances.append(str(instance))
        print(list_instances)

    def do_destroy(self, argv):
        args = argv.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = self.get_instance_key(args)
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[instance_key]
                storage.save()

    def do_update(self, argv):
        args = argv.split()
        if args == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = self.get_instance_key(args)
            if instance_key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = storage.all()[instance_key]
                attribute_name = args[2]
                value = args[3]
                setattr(instance, attribute_name, value)
                storage.save()

    def get_instance_key(self, args):
        """Helper method to get the instance key"""
        class_name = args[0]
        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        return instance_key


if __name__ == '__main__':
    HBNBCommand().cmdloop()
