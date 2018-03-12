# Claye
from validators.validator import Validator as Va
from washers.washer import Washer as Wa


class ValidateBmi(object):

    def is_valid(self, to_check):
        result = False
        list_bmi = ['Obesity', 'Overweight', 'Normal', 'Underweight']
        g = to_check
        g = Wa.wash_all_but_string_characters(g)
        g = Wa.set_case(g)
        if Va.is_in_list(g, list_bmi):
            result = True
        return g, result
