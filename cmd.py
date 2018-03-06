import sys
import validate_empid


class Check():
    def __init__(self):
        print("!!! Class Check Reached !!!")

    @staticmethod
    def empid():
        i = validate_empid.ValidateEmpid
        output = i.is_valid(i, "a#2@$&*(@&$01")
        if output:
            print("Valid ID")
        else:
            print("Invalid ID")

class CommandLine():
    user_command = input("> ")

    split_command = user_command.split(" ")

    class_to_call = split_command[0].title()
    method_to_call = ""
    string_to_send = ""

    if len(split_command) > 1:
        method_to_call = split_command[1].lower()
        if len(split_command) > 2:
            string_to_send = split_command[2]

    if class_to_call:
        try:
            class_name = getattr(sys.modules[__name__], class_to_call)
            class_name()
        except AttributeError:
            print("The command '{}' is not valid. Please enter Help to see a list of valid commands.".format(method_to_call))

    if method_to_call:
        try:
            class_name = getattr(sys.modules[__name__], class_to_call)
            method_name = getattr(class_name, method_to_call)
            method_name()
        except AttributeError:
            print("The switch '{}' is not valid.".format(method_to_call))

i = CommandLine()