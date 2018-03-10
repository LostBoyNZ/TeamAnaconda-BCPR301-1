# Claye
from validator import Validator as Va
from washer import Washer as Wa


class ValidateAge(object):

    def __init__(self, gender):
        self.gender = gender

    def is_valid(self):
        result = False
        gender_list_m = ['M', 'Boy', 'Male', 'Dude']
        gender_list_f = ['F', 'Girl', 'Female', 'Lady']
        g = self.gender
        g = Wa.wash_all_but_string_characters(g)
        g = Wa.set_case(g)
        if Va.is_in_list(g, gender_list_m):
            g = 'M'
        elif Va.is_in_list(g, gender_list_f):
            g = 'F'
        else:
            g = "INVALID"
        print("result: " + str(result))
        return g


i = ValidateAge(' 4254 54  M ale  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateAge(' 4254 54  L231Ady  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateAge(' 4254 54  fale  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateAge(' 4254 54  !fem ale  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateAge(' 4254 54  b !oy  $#$@13%$5 14-')
print(i.is_valid())

