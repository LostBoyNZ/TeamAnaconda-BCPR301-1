import re

class ValidateEmpid(object):

    data = ""

    def remove_symbol(self):
        characters_to_keep = re.compile(r"[^a-zA-Z0-9]")
        self.data = characters_to_keep.sub("", self.data)

    def set_case(self):
        self.data = self.data.title()

    def is_longer_than(self, max_length):
        is_too_long = False

        if len(self.data) > max_length:
            is_too_long = True

        return is_too_long

    def is_shorter_than(self, min_length):
        is_too_short = False

        if len(self.data) < min_length:
            is_too_short = True

        return is_too_short

    def contains_this_many_numbers(self, count):
        number_count = sum(a_character.isdigit() for a_character in self.data)
        return number_count == count

    def contains_this_many_letters(self, count):
        letter_count = sum(a_character.isalpha() for a_character in self.data)

        return letter_count == count

    def is_correct_format(self):
        result = False

        result = re.match(self.data, "^ [a - zA - Z][0 - 9]{3}$")

        return result

    def wash_data(self, to_wash):

        return to_wash

    def is_valid(self, data):
        self.data = data
        correct_length = False
        correct_number_of_characters = False
        correct_characters = False

        self.remove_symbol()
        self.set_case()

        if self.is_longer_than(4) == False and self.is_shorter_than(4) == False:
            correct_length = True

        if self.contains_this_many_numbers(3) == True and self.contains_this_many_letters(1) == True:
            correct_number_of_characters = True

        if self.data.isalnum() == True:
            correct_characters = True

        return correct_length and correct_number_of_characters and correct_characters

i = ValidateEmpid()
result = i.is_valid("a#2@$&*(@&$01")
print(i.data)
print(re.match(i.data, "^ [a - zA - Z][0 - 9]{3}$"))
print(result)
