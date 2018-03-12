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
                    result = Va.is_within_length(self.min_length, self.max_length, str(sales))
            elif isinstance(int(Wa.keep_only_nums(sales)), int):
                if Wa.strip_string(sales):
                    sales = Wa.keep_only_nums(sales)
                    sales = Wa.to_string(sales, self.min_length)
                    if Va.is_minimum(sales, self.min_sales):
                        result = Va.is_within_length(self.min_length, self.max_length, str(sales))
            else:
                result = False
            return sales, result
        except ValueError:
            result = False
            return sales, result
