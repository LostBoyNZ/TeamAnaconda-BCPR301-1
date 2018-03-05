import re

class Validator(object):
    # Graham
    @staticmethod
    def is_within_length(min_length, max_length, data):
        result = False

        if len(data) >= min_length and len(data) <= max_length:
            result = True

        return result

    # Graham
    @staticmethod
    def is_correct_pattern(target_pattern, data):
        result = False

        if re.match(target_pattern, data):
            result = True

        return result

    # Graham
    @staticmethod
    def has_this_many_numbers(count, data):
        number_count = sum(a_number.isdigit() for a_number in data)

        return number_count == count

    # Graham
    @staticmethod
    def has_this_many_letters(count, data):
        letter_count = sum(a_character.isalpha() for a_character in data)

        return letter_count == count

    # Claye
    @staticmethod
    def is_in_list(data, listed):
        if any(data in s for s in listed):
            result = True
        else:
            result = False
        return result


i = Validator()
