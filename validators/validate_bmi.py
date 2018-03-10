# Claye
from anaconda.validator import Validator as Va
from anaconda.washer import Washer as Wa


class ValidateBmi(object):

    def __init__(self, bmi):
        self.bmi = bmi

    def is_valid(self):
        result = False
        list_bmi = ['Obesity', 'Overweight', 'Normal', 'Underweight']
        g = self.bmi
        g = Wa.wash_all_but_string_characters(g)

        g = Wa.set_case(g)
        if Va.is_in_list(g, list_bmi):
            pass
        else:
            g = "INVALID"
        print("result: " + str(result))
        print(g)
        return g


i = ValidateBmi(' 4254 54  Obe sity  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateBmi(' 4254 54  Nor232323mal  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateBmi(' 4254 54  /underweirght  $#$@13%$5 14-')
print(i.is_valid())

i = ValidateBmi(' 4254 54  Under!@#5weight $#$@13%$5 14-')
print(i.is_valid())

i = ValidateBmi(' 4254 54  over Wei2352gh$@#$t  $#$@13%$5 14-')
print(i.is_valid())

