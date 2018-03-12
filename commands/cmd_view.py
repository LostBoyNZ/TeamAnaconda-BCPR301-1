# Rochelle

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


class View(Command):
    """
    Description:
        Fetches data from a file, counts the data and sends to the appropriate chart for output.

    VIEW /L /B /P /? [datatype]

    /L	Show line chart [sales] or [salary]
    /B  Show bar chart [bmi] or [birthday]
    /P  Show pie chart [age] or [gender]
    /?	Help about the View command

    [datatype]
    	Specifies the datatype to display the chart for
    """

    # do a prompt
    # translates switches into the method names, e.g. /q switch would run quit
    def get_switch(self, switch):
        return {
            'l': self._line,
            'b': self._bar,
            'p': self._pie,
            '?': self._help
        }.get(switch, '')

    def get_data(self):
        pass
    # get data for counting

    def count_data(self):
        pass
    # count data

    def test(self):
        print("TEST")

    # put the default action for this class (no switches used) here
    def _default(self):
        self._help()
        # cbi.ChartBirthday([3, 2, 7, 6, 5, 2, 1, 10, 4, 9, 6, 3])
        # cbm.
    #         send to self.help so they know what to input

    # put the methods for each switch here
    def _line(self):
        pass
    #     line chart for sales and salary

    def _bar(self):
        print("Bye bye!")
    #     bar chart for birthday or bmi

    def _pie(self):
        print("Bye bye!")
    #     gender and age

    def _message(self):
        print(self.user_string)
    #   salary, sales, age, bmi, birthday, gender

    def _help(self):
        print(self.__doc__)