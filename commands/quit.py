import sys

from commands.command import Command


class Quit(Command):
    """
    Docstring to be read as the help file for this command
    __doc__ & help()

    QUIT [/Q]
    /Q      Quiet mode, do not ask for confirmation before quitting
    """

    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'q': self.quit,
            'b': self.bye,
            'm': self.message
        }.get(switch, '')

    # put the default action for this class (no switches used) here
    def default(self):
        if self.my_command_line.confirm("quit"):
            self.quit()

    # put the methods for each switch here
    def quit(self):
        sys.exit()

    def bye(self):
        print("Bye bye!")

    def message(self):
        print(self.user_string)
