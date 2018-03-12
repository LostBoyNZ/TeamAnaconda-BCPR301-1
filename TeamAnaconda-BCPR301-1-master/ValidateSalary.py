# Rochelle
import re
from num2words import num2words
from word2number import w2n


class ValidateSalary(object):
    # write comments to explain!!!!!!!!!!!
    def __init__(self, salary):
        self.salary = salary
        self.lower_bound = 0
        self.upper_bound = 10000

    @staticmethod
    def keep_letters(salary):
        keep = re.compile(r"[^a-zA-Z- ]")
        salary = keep.sub("", salary)
        salary = salary.lstrip()
        salary = salary.rstrip()
        return salary

    @staticmethod # do these need to be static????
    def keep_nums(salary):
        keep = re.compile(r"[^0-9]")
        salary = keep.sub("", salary)
        return salary

    def is_within_boundaries(self, salary):
        if self.lower_bound < salary < self.upper_bound:
            return True
        else:
            return False

    def is_string(self, salary):
        salary = self.keep_letters(salary)
        salary = salary.lower()
        try:
            word = num2words(w2n.word_to_num(salary))
            print(word)
            print(salary)
            if self.is_within_boundaries(w2n.word_to_num(salary)) and salary == word:
                result = True
            else:
                result = False
        except ValueError:
            result = False

        return result

    def is_valid(self):
        salary = self.salary
        try:
            if isinstance(salary, int):
                result = self.is_within_boundaries(salary)
            elif isinstance(int(self.keep_nums(salary)), int):
                result = self.is_within_boundaries(int(self.keep_nums(salary)))
            else:
                result = False
        except ValueError:
            if isinstance(salary, str):
                result = self.is_string(salary)
            else:
                result = False
        # create more exceptions!!
        return result

    # need to have wash_data function
    # need to put functions into validator/washer and import them

# remove spaces from start and end of data
# allow for spaces inside of the word, can only have 3 spaces in middle, 1 between each word


i = ValidateSalary('nine hundred and thirty-five')
print(i.is_valid())
