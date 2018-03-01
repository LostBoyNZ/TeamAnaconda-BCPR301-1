# Rochelle
from num2words import num2words
from word2number import w2n
import re


class ValidateAge(object):

    def __init__(self, age):
        self.age = age

    def remove_symbol(self, age):
        remove = re.compile(r"[^a-zA-Z0-9-]")
        age = remove.sub("", age)
        return age

    def is_within_boundaries(self, age):
        lower = 0
        upper = 100
        if lower < age < upper:
            return True
        else:
            return False

    def calc_string(self, age):
        age = age.lower()
        age = self.remove_symbol(age)
        return age

    def is_string(self, age):
        age = self.calc_string(age)
        try:
            word = num2words(w2n.word_to_num(age))
            if self.is_within_boundaries(w2n.word_to_num(age)) and age == word:
                result = True
            else:
                result = False
        except ValueError:
            result = False

        return result

    def is_valid(self):
        age = self.age
        if isinstance(age, int):
            result = self.is_within_boundaries(age)
        elif isinstance(age, str):
            result = self.is_string(age)
        else:
            result = False

        return result

    # def wash_data(self, to_wash):
    # code for when its a number in a string e..g '56'

# try except for int


i = ValidateAge(67)
print(i.is_valid())
