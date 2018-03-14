from error_dict import ErrorDict
from databases.pickler_sqlite import Pickle


class ErrorHandler(object):  # Claye

    @staticmethod
    def get_error_message(error_code, name=""):

        error_dict = ErrorDict.get_error_dict(name)

        try:
            return error_dict[error_code]
        except KeyError:
            return "Unknown Error"

    @staticmethod
    def send_data_to_pickler():
        to_pickle = ErrorDict.get_error_dict('')
        pickled = Pickle.pickle_list(to_pickle)
        return pickled
