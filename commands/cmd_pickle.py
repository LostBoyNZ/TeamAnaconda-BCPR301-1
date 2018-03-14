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
    print(err.get_error_message(404, "command"))
    sys.exit()

try:
    from log_file_handler import LogFileHandler as lfh
except NameError and ModuleNotFoundError and ImportError:
    print(err.get_error_message(404, "log_file_handler"))
    sys.exit()

try:
    from databases.pickler_sqllite import Pickle as pkl
except NameError and ModuleNotFoundError and ImportError:
    print(err.get_error_message(404, "pickler_sqllite"))
    sys.exit()


class Pickle(Command):
    '''
    adsfdsafdsfdf

    PICKE

    /A  adsfdsfdafd
    '''
    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'p': self._pickle,
            'u': self._unpickle,
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):
        pass

    def _pickle(self):
        pass

    def _unpickle(self):
        pass

    def _help(self):
        print(self.__doc__)
