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
            from views.console_view import ConsoleView as cv
        except NameError and ModuleNotFoundError and ImportError:
            print(err.get_error_message(250, "console_view"))
            sys.exit()

        try:
            from cmd import CommandLine as cmd
        except NameError and ModuleNotFoundError and ImportError:
            print(err.get_error_message(250, "cmd"))
            sys.exit()

        print("loading command line...")
        cmd()

i = Start()
