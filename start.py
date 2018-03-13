# Graham
import sys


class Start:
    """
    Python Database Handler [Version 1.0]
    (c) 2018 Team Anaconda Ltd, all rights reserved.

    Authors: Claye Barry, Rochelle Wilson, Graham Parker

    """
    def __init__(self):

        try:
            from errors import ErrorHandler as err
        except NameError and ModuleNotFoundError and ImportError:
            print("Fatal Error - errors.py not found.")
            sys.exit()

        try:
            from cmdline import CommandLine as cmd
        except NameError and ModuleNotFoundError and ImportError:
            print(err.get_error_message(404, "cmd"))
            sys.exit()

        print(self.__doc__)
        cmd().run_commandline()


i = Start()
