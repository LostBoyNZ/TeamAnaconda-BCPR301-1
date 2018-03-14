# Graham
import sys
import os


class Start:
    """
    Python Database Handler [Version 1.0]
    (c) 2018 Team Anaconda Ltd, all rights reserved.

    Authors: Claye Barry, Rochelle Wilson, Graham Parker

    """
    def __init__(self):

        print("Loading...")

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

        os.system('cls')
        print(self.__doc__)

        user_args = []
        try:
            user_args = sys.argv[1:]
        except TypeError:
            pass

        cmd().run_commandline(user_args)

i = Start()
