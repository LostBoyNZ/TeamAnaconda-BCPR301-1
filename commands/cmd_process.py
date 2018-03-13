# Claye

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


class Process(Command):
    """
        Fetches data from a file, validates the data and saves the washed data into a local file.

        PROCESS [/D]

        -D		Display details of data validation

        Supported file formats include:
            .txt
            .csv
    """

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'd': self._detail,
            '?': self._help
        }.get(switch, '')

    # put an action here which will always run first, switch or no switch
    def _always_run(self):
        pass

    # put the default action for this class (no switches used) here
    def _default(self):
        i = FileReader()
        FileReader.call_file(i, '')

    # put the methods for each switch here
    def _detail(self):
        i = FileReader()
        FileReader.call_file(i, 'd')

    def _help(self):
        print(self.__doc__)

