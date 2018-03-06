# Rochelle
import re
from num2words import num2words
from word2number import w2n


class ValidateSales(object):
# write comments to explain!!!!!!!!!!!
    def __init__(self, sales):
        self.sales = sales
        self.lower_bound = 0
        self.upper_bound = 1000

    @staticmethod
    def keep_letters(sales):
        keep = re.compile(r"[^a-zA-Z- ]")
        sales = keep.sub("", sales)
        sales = sales.lstrip()
        sales = sales.rstrip()
        return sales

    @staticmethod # do these need to be static????
    def keep_nums(sales):
        keep = re.compile(r"[^0-9]")
        sales = keep.sub("", sales)
        return sales

    def is_within_boundaries(self, sales):
        if self.lower_bound < sales < self.upper_bound:
            return True
        else:
            return False

    def is_string(self, sales):
        sales = self.keep_letters(sales)
        sales = sales.lower()
        try:
            word = num2words(w2n.word_to_num(sales))
            print(word)
            print(sales)
            if self.is_within_boundaries(w2n.word_to_num(sales)) and sales == word:
                result = True
            else:
                result = False
        except ValueError:
            result = False

        return result

    def is_valid(self):
        sales = self.sales
        try:
            if isinstance(sales, int):
                result = self.is_within_boundaries(sales)
            elif isinstance(int(self.keep_nums(sales)), int):
                result = self.is_within_boundaries(int(self.keep_nums(sales)))
            else:
                result = False
        except ValueError:
            if isinstance(sales, str):
                result = self.is_string(sales)
            else:
                result = False
        # create more exceptions!!
        return result

    # need to have wash_data function
    # need to put functions into validator/washer and import them

# remove spaces from start and end of data s = s.lstrip() s = s.rstrip()
# allow for spaces inside of the word, can only have 3 spaces in middle, 1 between each word


i = ValidateSales('             nine hundred and thirty-five             ')
print(i.is_valid())
