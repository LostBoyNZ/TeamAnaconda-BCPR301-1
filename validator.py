import re

class Validator(object):
    # Graham
    def is_within_length(min_length, max_length, data):
        result = False

        if len(data) >= min_length and len(data) <= max_length:
            result = True

        return result

    # Graham
    def is_correct_pattern(target_pattern, data):
        result = False

        if re.match(target_pattern, data):
            result = True

        return result

    # Graham
    def has_this_many_numbers(count, data):
        number_count = sum(a_number.isdigit() for a_number in data)

        return number_count == count

    # Graham
    def has_this_many_letters(count, data):
        letter_count = sum(a_character.isalpha() for a_character in data)

        return letter_count == count

    # Claye
    def is_in_list(data, listed):
        if any(data in s for s in listed):
            result = True
        else:
            result = False

        return result

    # Rochelle
    def is_minimum(data, minimum):
        result = False
        if int(data) >= minimum:
            result = True
        return result
