import validator
import washer

class ValidateEmpid(object):

    @staticmethod
    def wash_data(data_to_wash):
        washed_data = washer.Washer.keep_only_these_in_string("a-zA-Z0-9", data_to_wash)
        washed_data = washer.Washer.set_case(washed_data)

        return washed_data

    def is_valid(self, data_to_validate):
        correct_length = False
        correct_number_of_characters = False
        correct_characters = False
        correct_format = False

        # Wash the data before verifying it
        data_to_validate = self.wash_data(data_to_validate)

        # \D where a non-number should be, and \d where a number should be
        if validator.Validator.is_correct_pattern("\D\d\d\d", data_to_validate) == True:
            correct_format = True

        if validator.Validator.is_within_length(4, 4, data_to_validate) == True:
            correct_length = True

        if validator.Validator.has_this_many_numbers(3, data_to_validate) == True and validator.Validator.has_this_many_letters(1, data_to_validate) == True:
            correct_number_of_characters = True

        if data_to_validate.isalnum() == True:
            correct_characters = True

        return correct_length and correct_number_of_characters and correct_characters and correct_format

i = ValidateEmpid()
result = i.is_valid("a#2@$&*(@&$01")
print(result)