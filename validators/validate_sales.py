# Rochelle
from validators.validator import Validator as Va
from washers.washer import Washer as Wa

class ValidateSales(object):
# write comments to explain!!!!!!!!!!!
    def __init__(self):
        self.min_sales = 0
        self.min_length = 3
        self.max_length = 3

    def is_valid(self, sales):
        result = False
        try:
            if isinstance(sales, int):
                sales = Wa.to_string(sales, self.min_length)
                if Va.is_minimum(sales, self.min_sales):
                    result = Va.is_within_length(Va, self.min_length, self.max_length, str(sales))
            elif isinstance(int(Wa.keep_only_nums(sales)), int):
                if Wa.strip_string(sales):
                    sales = Wa.keep_only_nums(sales)
                    sales = Wa.to_string(sales, self.min_length)
                    if Va.is_minimum(sales, self.min_sales):
                        result = Va.is_within_length(Va, self.min_length, self.max_length, str(sales))
            else:
                result = False
            return sales, result
        except ValueError:
            result = False
            return sales, result


i = ValidateSales()
print(1, i.is_valid('@$    9  ^&dbnd  '))

i = ValidateSales()
print(2, i.is_valid('       #$%@$     90 adddfh'))

i = ValidateSales()
print(3, i.is_valid(                 9  ))

i = ValidateSales()
print(4, i.is_valid(   999))

i = ValidateSales()
print(5, i.is_valid('  nine hundred and thirty five  '))

i = ValidateSales()
print(6, i.is_valid('  10'))

i = ValidateSales()
print(7, i.is_valid('  1= '))

i = ValidateSales()
print(8, i.is_valid('  -1 '))

i = ValidateSales()
print(9, i.is_valid('  111 '))
