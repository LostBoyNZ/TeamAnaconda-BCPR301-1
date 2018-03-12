# Rochelle
from validators.validator import Validator as Va
from washers.washer import Washer as Wa


class ValidateAge(object):

    def __init__(self):
        self.min_age = 1
        self.min_length = 2
        self.max_length = 2

    def is_valid(self, age):
        result = False
        try:
            if isinstance(age, int):
                age = Wa.to_string(age, self.min_length)
                if Va.is_minimum(age, self.min_age):
                    result = Va.is_within_length(Va, self.min_length, self.max_length, str(age))
            elif isinstance(int(Wa.keep_only_nums(age)), int):
                if Wa.strip_string(age):
                    age = Wa.keep_only_nums(age)
                    age = Wa.to_string(age, self.min_length)
                    if Va.is_minimum(age, self.min_age):
                        result = Va.is_within_length(Va, self.min_length, self.max_length, str(age))
            return age, result
        except ValueError:
            result = False
            return age, result
