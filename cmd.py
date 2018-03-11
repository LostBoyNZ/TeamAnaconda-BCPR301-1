# Graham

import sys

_show_non_fatal_errors = True

try:
    from errors import ErrorHandler as err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()

try:
    from views.console_view import ConsoleView as cv
except NameError and ModuleNotFoundError and ImportError:
    print(err.get_error_message(250, "console_view"))
    sys.exit()

try:
    from commands.quit import Quit
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(250, "quit"))
    pass


class CommandLine:

    prompt = ""

    def __init__(self):
        #Cmd.__init__(self)
        self.prompt = "> "

    def run_commandline(self):
        while True:
            self._get_command()

    def _get_command(self):
        user_command = cv.get_input(self.prompt)
        self._split_command(user_command)

    def _split_command(self, user_command):
        switches_and_data = ""

        # split the command at the start, from the entire string
        split_input = user_command.split(" ", 1)
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
                cv.show_output(
                    "The command '{}' is not valid. Please enter 'Help' for a list of commands.".format(class_to_call))

    def confirm(self, action_name):
        result = False
        prompt = "Are you sure you want to {}? Y/N".format(action_name)
        user_input = cv.get_input(prompt)

        if user_input[0].lower() == "y":
            result = True

        return result

i = CommandLine()

i.run_commandline()
