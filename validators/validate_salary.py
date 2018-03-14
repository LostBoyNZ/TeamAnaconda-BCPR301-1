# Rochelle
from validators.validator import Validator as Va
from washers.washer import Washer as Wa



class ValidateSalary(object):
    def __init__(self):
        self.min_salary = 0
        self.min_length = 2
        self.max_length = 3

    def is_valid(self, salary):
        """
        >>> i = ValidateSalary()
        >>> i.is_valid("gfdjhs804")
        ('804', True)
        >>> i.is_valid(1000)
        ('1000', False)
        >>> i.is_valid('  RFGVHJ#$%^&*  6       @#$%^&*(DFGHJ')
        ('06', True)
        >>> i.is_valid(' twenty-two ')
        (' twenty-two ', False)
        :param salary:
        :return:
        """
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