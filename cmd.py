# fix these to from ... import ...
import sys
import console_view
import validate_empid

class Check():
    """
    Docstring to be read as the help file for this command
    __doc__ & help()
    """
    def __init__(self):
        console_view.ConsoleView.show_output("!!! Class Check Reached !!!")

    @staticmethod
    def empid():
        """ docstring goes here"""
        i = validate_empid.ValidateEmpid
        output = i.is_valid(i, "a#2@$&*(@&$01")
        if output:
            console_view.ConsoleView.show_output("Valid ID")
        else:
            console_view.ConsoleView.show_output("Invalid ID")

class Quit():
    """
    Docstring to be read as the help file for this command
    __doc__ & help()
    """
    def __init__(self):
        """ docstring goes here"""
        wants_to_quit = console_view.ConsoleView.get_input("Are you sure you want to quit? Y/N").lower()
        if wants_to_quit[0] == "y":
            sys.exit()

#class CommandLine(cmd)
class CommandLine():

    def __init__(self):
        #Cmd.__init__(self)
        self.prompt = "> "

    def run_commandline(self):
        while True:
            self.get_input()

    def get_input(self):
        user_command = console_view.ConsoleView.get_input(self.prompt)
        self._split_input(user_command)

    def _split_input(self, user_command):
        split_command = user_command.split(" ")
        class_to_call = split_command[0].title()
        method_to_call = ""
        string_to_send = ""

        if len(split_command) > 1:
            method_to_call = split_command[1].lower()
            if len(split_command) > 2:
                string_to_send = split_command[2]

        self._process_command(class_to_call, method_to_call, string_to_send)

    def _process_command(self, class_to_call, method_to_call, string_to_send):
        if class_to_call:
            try:
                class_name = getattr(sys.modules[__name__], class_to_call)
                class_name()
            except AttributeError:
                console_view.ConsoleView.show_output(
                    "The command '{}' is not valid. Please enter 'Help' for a list of commands.".format(class_to_call))

        if method_to_call:
            try:
                class_name = getattr(sys.modules[__name__], class_to_call)
                method_name = getattr(class_name, method_to_call)
                method_name()
            except AttributeError:
                console_view.ConsoleView.show_output("The switch '{}' is not valid.".format(method_to_call))

i = CommandLine()

i.run_commandline()
