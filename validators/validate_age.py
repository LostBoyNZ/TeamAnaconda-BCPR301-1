# Rochelle
from validator import Validator as Va
from washer import Washer as Wa


class ValidateAge(object):

    def __init__(self, age):
        self.age = age
        self.min_age = 1
        self.min_length = 2
        self.max_length = 2

    def is_valid(self):
        age = self.age
        result = False
        try:
            if isinstance(age, int):
                self.age = Wa.to_string(age, self.min_length)
                if Va.is_minimum(self.age, self.min_age):
                    result = Va.is_within_length(Va, self.min_length, self.max_length, str(self.age))
            elif isinstance(int(Wa.keep_only_nums(age)), int):
                if Wa.strip_string(age):
                    age = Wa.keep_only_nums(age)
                    self.age = Wa.to_string(age, self.min_length)
                    if Va.is_minimum(self.age, self.min_age):
                        result = Va.is_within_length(Va, self.min_length, self.max_length, str(self.age))
            else:
                self.age = age
                result = False
            return self.age, result
        except ValueError:
            result = False
            self.age = age
            return self.age, result


i = ValidateAge('@$    9  ^&dbnd  ')
print(1, i.is_valid())

i = ValidateAge('       #$%@$     90 adddfh'                )
print(2, i.is_valid())

i = ValidateAge(                 9  )
print(3, i.is_valid())

i = ValidateAge(   99)
print(4, i.is_valid())

i = ValidateAge('  nine  ')
print(5, i.is_valid())

i = ValidateAge(' #@!$%*( twenty-nine ')
print(6, i.is_valid())

i = ValidateAge(' !$%*( twenty nine')
print(7, i.is_valid())

i = ValidateAge(100)
print(8, i.is_valid())

i = ValidateAge(0)
print(9, i.is_valid())

i = ValidateAge('0')
print(10, i.is_valid())

i = ValidateAge(1)
print(12, i.is_valid())

i = ValidateAge('1')
print(13, i.is_valid())
