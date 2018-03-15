# Graham

import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from commands.command import Command
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - command.py in commands folder not found.")


class Quit(Command):
    """
    Exits the software with a prompt to confirm.

    QUIT [/?] [/Q]

    /Q	Quiet mode disables the confirmation prompt
    /?	Help about the Quit command
    """

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'q': self._quit,
            'b': self._bye,
            'm': self._message,
            '?': self._help
        }.get(switch, '')

    def test(self):
        print("TEST")

    # put the default action for this class (no switches used) here
    def _default(self):
        if self.my_command_line.confirm("quit"):
            self._quit()

    # put the methods for each switch here
    def _quit(self):
        sys.exit()

    def _bye(self):
        print("Bye bye!")

    def _message(self):
        print(self.user_string)

    def _help(self):
        print(self.__doc__)
