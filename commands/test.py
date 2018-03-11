# Graham

import sys

try:
    from errors import ErrorHandler as err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()

try:
    from commands.command import Command
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - command.py in commands folder not found.")

try:
    from file_reader import FileReader
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - file_reader.py in commands folder not found.")


class Test(Command):
    '''
    Docstring to be read as the help file for this command
    __doc__ & help()

    QUIT [/Q]
    /Q      Quiet mode, do not ask for confirmation before quitting
    '''

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'q': self._quit,
            'b': self._bye,
            'm': self._message,
            '?': self._help
        }.get(switch, '')

    # put an action here which will always run first, switch or no switch
    def _always_run(self):
        pass

    # put the default action for this class (no switches used) here
    def _default(self):
        i = FileReader()
        FileReader.call_file(i)

    # put the methods for each switch here
    def _quit(self):
        sys.exit()

    def _bye(self):
        print("Bye bye!")

    def _message(self):
        print(self.user_string)

    def _help(self):
        print(help(Test))