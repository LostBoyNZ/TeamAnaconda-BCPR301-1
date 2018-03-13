# Graham

_show_non_fatal_errors = True

import sys

try:
    from errors import ErrorHandler as err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()

try:
    from views.console_view import ConsoleView as cv
except NameError and ModuleNotFoundError and ImportError:
    print(err.get_error_message(404, "console_view"))
    sys.exit()

try:
    from commands.cmd_quit import Quit
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(403, "quit"))
    pass

try:
    from commands.cmd_help import Help
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(403, "help"))
    pass

try:
    from commands.cmd_process import Process
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(403, "process"))
    pass

try:
    from commands.cmd_log import Log
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(403, "log"))
    pass

try:
    from commands.cmd_log import Log
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(403, "log"))
    pass
	
try:
    from commands.cmd_view import View
except NameError and ModuleNotFoundError and ImportError:
    if _show_non_fatal_errors:
        print(err.get_error_message(403, "view"))
    pass


class CommandLine:

    prompt = ""

    def __init__(self):
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
            switches_and_data = split_input[1].lower()

        self._process_command(class_to_call, switches_and_data)

    def _process_command(self, class_to_call, switches_and_data):
        if class_to_call:
             # try:
                class_name = getattr(sys.modules[__name__], class_to_call)
                class_name(switches_and_data, self)
             # except AttributeError:
             #     cv.show_output(
             #         "The command '{}' is not valid. Please enter 'Help' for a list of commands.".format(class_to_call))

    def confirm(self, action_name):
        result = False
        prompt = "Are you sure you want to {}? Y/N".format(action_name)
        user_input = cv.get_input(prompt)

        try:
            if user_input[0].lower() == "y":
                result = True
        except IndexError:
            print(err.get_error_message(102))
            self.confirm(action_name)

        return result
