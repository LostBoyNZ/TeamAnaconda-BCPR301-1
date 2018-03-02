import re

class Validator(object):
    # Graham
    def is_within_length(self, min_length, max_length):
        correct = False

        if len(self.data) >= min_length and len(self.data) <= max_length:
            correct = True

        return correct

    # Graham
    def is_correct_pattern(self, data, target_pattern):
        is_correct = False

        if re.match(target_pattern, data):
            is_correct = True

        return is_correct

    # Graham
    def has_this_many_numbers(self, data, count):
        number_count = sum(a_number.isdigit() for a_number in data)

        return number_count == count

    # Graham
    def has_this_many_letters(self, data, count):
        letter_count = sum(a_character.isalpha() for a_character in data)

        return letter_count == count

    # Claye
    def is_in_list(self, data, listed):
        if any(data in s for s in listed):
            result = True
        else:
            result = False
        return result


i = Validator()
