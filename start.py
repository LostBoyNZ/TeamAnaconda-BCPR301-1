# Graham
import sys


class Start():

    def __init__(self):

        try:
            from errors import ErrorHandler as err
        except NameError and ModuleNotFoundError and ImportError:
            print("Fatal Error - errors.py not found.")
            sys.exit()

        try:
            from cmd import CommandLine as cmd
        except NameError and ModuleNotFoundError and ImportError:
            print(err.get_error_message(404, "cmd"))
            sys.exit()

        cmd().run_commandline()

i = Start()
