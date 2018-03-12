# Rochelle
from validators.validator import Validator as Va
from washers.washer import Washer as Wa


class ValidateSales(object):
# write comments to explain!!!!!!!!!!!
    def __init__(self, sales):
        self.sales = sales
        self.min_sales = 0
        self.min_length = 3
        self.max_length = 3

    def is_valid(self):
        sales = self.sales
        result = False
        try:
            if isinstance(sales, int):
                self.sales = Wa.to_string(sales, self.min_length)
                if Va.is_minimum(self.sales, self.min_sales):
                    result = Va.is_within_length(Va, self.min_length, self.max_length, str(self.sales))
            elif isinstance(int(Wa.keep_only_nums(sales)), int):
                if Wa.strip_string(sales):
                    sales = Wa.keep_only_nums(sales)
                    self.sales = Wa.to_string(sales, self.min_length)
                    if Va.is_minimum(self.sales, self.min_sales):
                        result = Va.is_within_length(Va, self.min_length, self.max_length, str(self.sales))
            else:
                self.sales = sales
                result = False
            return self.sales, result
        except ValueError:
            result = False
            self.sales = sales
            return self.sales, result


i = ValidateSales('@$    9  ^&dbnd  ')
print(1, i.is_valid())

i = ValidateSales('       #$%@$     90 adddfh'                )
print(2, i.is_valid())

i = ValidateSales(                 9  )
print(3, i.is_valid())

i = ValidateSales(   999)
print(4, i.is_valid())

i = ValidateSales('  nine hundred and thirty five  ')
print(5, i.is_valid())

i = ValidateSales('  10')
print(6, i.is_valid())

i = ValidateSales('  1= ')
print(7, i.is_valid())

i = ValidateSales('  -1 ')
print(8, i.is_valid())

i = ValidateSales('  111 ')
print(9, i.is_valid())
