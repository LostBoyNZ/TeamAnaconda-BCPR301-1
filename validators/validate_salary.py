# Rochelle
# from validators.validator import Validator as Va
# from washers.washer import Washer as Wa
from validator import Validator as Va
from washer import Washer as Wa


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


i = ValidateSalary()
print(1, i.is_valid('@$    9  ^&dbnd  '))

i = ValidateSalary()
print(2, i.is_valid('       #$%@$     90 adddfh'))

i = ValidateSalary()
print(3, i.is_valid(9))

i = ValidateSalary()
print(4, i.is_valid(999))

i = ValidateSalary()
print(5, i.is_valid('  nine hundred and thirty five  '))

i = ValidateSalary()
print(6, i.is_valid('  10'))

i = ValidateSalary()
print(7, i.is_valid('  1= '))

i = ValidateSalary()
print(8, i.is_valid('  -1 '))

i = ValidateSalary()
print(9, i.is_valid('  111 '))

i = ValidateSalary()
print(10, i.is_valid('  22 '))

i = ValidateSalary()
print(11, i.is_valid('  222 '))
