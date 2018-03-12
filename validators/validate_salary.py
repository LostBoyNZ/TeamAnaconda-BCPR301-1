# Rochelle
from validators.validator import Validator as Va
from washers.washer import Washer as Wa


class ValidateSalary(object):
    # write comments to explain!!!!!!!!!!!
    def __init__(self, salary):
        self.salary = salary
        self.min_salary = 0
        self.min_length = 2
        self.max_length = 3

    def is_valid(self):
        salary = self.salary
        result = False
        try:
            if isinstance(salary, int):
                self.salary = Wa.to_string(salary, self.min_length)
                if Va.is_minimum(self.salary, self.min_salary):
                    result = Va.is_within_length(Va, self.min_length, self.max_length, str(self.salary))
            elif isinstance(int(Wa.keep_only_nums(salary)), int):
                if Wa.strip_string(salary):
                    salary = Wa.keep_only_nums(salary)
                    self.salary = Wa.to_string(salary, self.min_length)
                    if Va.is_minimum(self.salary, self.min_salary):
                        result = Va.is_within_length(Va, self.min_length, self.max_length, str(self.salary))
            else:
                self.salary = salary
                result = False
            return self.salary, result
        except ValueError:
            result = False
            self.salary = salary
            return self.salary, result


i = ValidateSalary('@$    9  ^&dbnd  ')
print(1, i.is_valid())

i = ValidateSalary('       #$%@$     90 adddfh')
print(2, i.is_valid())

i = ValidateSalary(9)
print(3, i.is_valid())

i = ValidateSalary(999)
print(4, i.is_valid())

i = ValidateSalary('  nine hundred and thirty five  ')
print(5, i.is_valid())

i = ValidateSalary('  10')
print(6, i.is_valid())

i = ValidateSalary('  1= ')
print(7, i.is_valid())

i = ValidateSalary('  -1 ')
print(8, i.is_valid())

i = ValidateSalary('  111 ')
print(9, i.is_valid())

i = ValidateSalary('  22 ')
print(10, i.is_valid())

i = ValidateSalary('  222 ')
print(11, i.is_valid())
