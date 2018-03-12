# Graham

import sys

try:
    #from validator import Validator, is_correct_pattern, is_within_length, has_this_many_numbers, has_this_many_letters
    from validators.validator import Validator
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - validator.py not found.")
    sys.exit()

try:
    #from washer import Washer, keep_only_these_in_string, set_case
    from washers.washer import Washer
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - washer.py not found.")
    sys.exit()


class ValidateEmpid():

    @staticmethod
    def is_valid(data_to_validate):
        correct_length = False
        correct_number_of_characters = False
        correct_characters = False
        correct_format = False

        # Wash the data before verifying it
        washed_data = Washer.keep_only_these_in_string("a-zA-Z0-9", data_to_validate)
        washed_data = Washer.set_case(washed_data)
        print(washed_data)
        # \D where a non-number should be, and \d where a number should be
        if Validator.is_correct_pattern("\D\d\d\d", washed_data) == True:
            correct_format = True

        if Validator.is_within_length(4, 4, washed_data) == True:
            correct_length = True

        if Validator.has_this_many_numbers(3, washed_data) == True and Validator.has_this_many_letters(1, washed_data) == True:
            correct_number_of_characters = True

        if washed_data.isalnum() == True:
            correct_characters = True

        print(correct_length)
        print(correct_number_of_characters)
        print(correct_characters)
        print(correct_format)
        is_valid = correct_length and correct_number_of_characters and correct_characters and correct_format
        id_output = washed_data
        print("----")
        print(is_valid)
        print(id_output)
        print("----")
        return id_output, is_valid
