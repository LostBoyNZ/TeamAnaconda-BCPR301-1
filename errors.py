from error_dict import ErrorDict
from databases.pickler import Pickler


class ErrorHandler(object):  # Claye

    @staticmethod
    def get_error_message(error_code, name=""):
        """
         >>> ErrorHandler.get_error_message(101)
         'Command not supported'

         >>> ErrorHandler.get_error_message(205)
         'Unable to edit log file'

         >>> ErrorHandler.get_error_message(404, 'test')
         'Fatal Error - test not found'

         >>> ErrorHandler.get_error_message(601)
         'Data in this chart type not supported'
        """

        error_dict = ErrorDict.get_error_dict(name)

        try:
            return error_dict[error_code]
        except KeyError:
            return "Unknown Error"

    @staticmethod
    def send_data_to_pickler():
        to_pickle = ErrorDict.get_error_dict('')
        pickled = Pickler.pickle_list(to_pickle)
        return pickled

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
