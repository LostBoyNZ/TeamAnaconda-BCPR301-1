# fix these to from ... import ...
import sys
import console_view
import validate_empid
import quit

class Check():
    """
    Docstring to be read as the help file for this command
    __doc__ & help()
    """

    my_command_line = None

    def __init__(self, user_data, command_line):
        """ docstring goes here"""
        self.my_command_line = command_line

        #if user_data

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

    QUIT [/Q]
    /Q      Quiet mode, do not ask for confirmation before quitting
    """

    my_command_line = None
    user_string = ""

    def __init__(self, switches_and_data, command_line):
        """ docstring goes here"""
        self.my_command_line = command_line

        # extract and run switch methods and extract user data, e.g. file name, from the command
        if switches_and_data:
            methods_to_run, self.user_string = self.my_command_line.split_input(switches_and_data, self)
            if methods_to_run:
                self.run_switch_methods(methods_to_run)

        # default action
        if self.my_command_line.confirm("quit"):
            self.quit()

    def run_switch_methods(self, methods_to_run):
        for method in methods_to_run:
            try:
                method()
            except TypeError:
                pass

    def get_switch(self, switch):
        return {
            'q': self.quit,
            'b': self.bye,
            'm': self.message
        }.get(switch, '')

    def quit(self):
        sys.exit()

    def bye(self):
        print("Bye bye!")

    def message(self):
        print(self.user_string)

class CommandLine():

    prompt = ""

    def __init__(self):
        #Cmd.__init__(self)
        self.prompt = "> "

    def run_commandline(self):
        while True:
            self.get_input()

    def get_input(self):
        user_input = console_view.ConsoleView.get_input(self.prompt)
        self._split_input(user_input)

    def _split_input(self, user_input):
        switches_and_data = ""

        # split the command at the start, from the entire string
        split_input = user_input.split(" ", 1)
        # capitalize the command as that's a class name to call
        class_to_call = split_input[0].title()

        # if there's any more to the string, that's switches and user data, e.g. a file name
        if len(split_input) > 1:
            switches_and_data = split_input[1]

        self._process_command(class_to_call, switches_and_data)

    def _process_command(self, class_to_call, switches_and_data):
        if class_to_call:
            try:
                method_to_call = "Go"
                class_name = getattr(sys.modules[__name__], class_to_call)
                class_name(switches_and_data, self)
            except AttributeError:
                console_view.ConsoleView.show_output(
                    "The command '{}' is not valid. Please enter 'Help' for a list of commands.".format(class_to_call))

    def confirm(self, action_name):
        result = False
        prompt = "Are you sure you want to {}? Y/N".format(action_name)
        user_input = console_view.ConsoleView.get_input(prompt)

        if user_input[0].lower() == "y":
            result = True

        return result

    def split_input(self, user_data, my_command):
        methods_to_run = []
        strings_to_keep = []
        split_user_data = user_data.split(" ")

        for data in split_user_data:
            if data[0] == "/" and len(data) == 2:
                switch = my_command.get_switch(data[1])
                methods_to_run.append(switch)
            else:
                not_a_switch = (data)
                strings_to_keep.append(not_a_switch)

        user_string = " ".join(strings_to_keep)
        return methods_to_run, user_string


i = CommandLine()

i.run_commandline()
