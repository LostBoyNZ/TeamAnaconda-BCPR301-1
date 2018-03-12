# Rochelle
from validators.validator import Validator as Va
from washers.washer import Washer as Wa



class ValidateSalary(object):
    # write comments to explain!!!!!!!!!!!
    def __init__(self):
        self.min_salary = 0
        self.min_length = 2
        self.max_length = 3

    def is_valid(self, salary):
        result = False
        try:
            if isinstance(salary, int):
                salary = Wa.to_string(salary, self.min_length)
                if Va.is_minimum(salary, self.min_salary):
                    result = Va.is_within_length(self.min_length, self.max_length, str(salary))
            elif isinstance(int(Wa.keep_only_nums(salary)), int):
                if Wa.strip_string(salary):
                    salary = Wa.keep_only_nums(salary)
                    salary = Wa.to_string(salary, self.min_length)
                    if Va.is_minimum(salary, self.min_salary):
                        result = Va.is_within_length(self.min_length, self.max_length, str(salary))
            else:
                result = False
            return salary, result
        except ValueError:
            result = False
            return salary, result
