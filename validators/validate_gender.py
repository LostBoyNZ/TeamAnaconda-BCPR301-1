# Claye
from validators.validator import Validator as Va
from washers.washer import Washer as Wa


class ValidateGender(object):

    def is_valid(self, to_check):
        result = False
        gender_list_m = ['M', 'Boy', 'Male', 'Dude']
        gender_list_f = ['F', 'Girl', 'Female', 'Lady']
        g = to_check
        g = Wa.wash_all_but_string_characters(g)
        g = Wa.set_case(g)
        if Va.is_in_list(g, gender_list_m):
            g = 'M'
            result = True
        elif Va.is_in_list(g, gender_list_f):
            g = 'F'
            result = True
        return g, result
