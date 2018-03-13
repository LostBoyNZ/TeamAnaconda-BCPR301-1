# Graham

_show_non_fatal_errors = True

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


class Log(Command):
    '''
    Outputs the lines of the log.txt file.

    LOG [/?] [/R]

    /R	Output the log file in reverse (latest on top)
    /W  Wipes the log file after confirmation
    /?	Help about the Quit command
    '''

    FILE_NAME = "log.txt"

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'a': self._append,
            'r': self._reverse,
            'w': self._wipe,
            '?': self._help
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def _default(self):

        file_contents = lfh.load_file_data(lfh, self.FILE_NAME)
        direction = ""
        if len(file_contents) == 0:
            print(err.get_error_message(208))

        lfh.output_file(lfh, file_contents, direction)

    def _append(self):
        lfh.append_file(self.FILE_NAME, self.user_string)

    def _reverse(self):
        file_contents = lfh.load_file_data(lfh, self.FILE_NAME)
        direction = "r"

        lfh.output_file(lfh, file_contents, direction)

    def _wipe(self):
        if self.my_command_line.confirm("wipe the log"):
            lfh.wipe_file(lfh, self.FILE_NAME)

    def _quiet_mode(self):
        self._quiet_mode = True

    def _help(self):
        print(self.__doc__)
