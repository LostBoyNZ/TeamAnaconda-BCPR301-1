# Rochelle
import re
from num2words import num2words
from word2number import w2n


class ValidateAge(object):

    def __init__(self, age):
        self.age = age

    @staticmethod
    def keep_letters(age):
        keep = re.compile(r"[^a-zA-Z-]")
        age = keep.sub("", age)
        return age

    @staticmethod
    def keep_nums(age):
        keep = re.compile(r"[^0-9]")
        age = keep.sub("", age)
        return age

    @staticmethod
    def is_within_boundaries(age):
        lower = 0
        upper = 100
        if lower < age < upper:
            return True
        else:
            return False

    def is_string(self, age):
        age = self.keep_letters(age)
        age = age.lower()
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
        try:
            if isinstance(age, int):
                result = self.is_within_boundaries(age)
            elif isinstance(int(self.keep_nums(age)), int):
                result = self.is_within_boundaries(int(self.keep_nums(age)))
            else:
                result = False
        except ValueError:
            if isinstance(age, str):
                result = self.is_string(age)
            else:
                result = False
        # create more exceptions!!
        return result

    # need to have wash_data function
    # need to put functions into validator/washer and import them


i = ValidateAge('   6g7   j*()   "'"")
print(i.is_valid())
