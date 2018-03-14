# Claye
from validators.validator import Validator as Va
from washers.washer import Washer as Wa


class ValidateBmi(object):
    @staticmethod
    def is_valid(to_check):
        """
        >>> ValidateBmi.is_valid('Obese')
        ('Obesity', True)
        >>> ValidateBmi.is_valid('norm3123123#@$@#$#@4al')
        ('Normal', True)
        >>> ValidateBmi.is_valid('person')
        ('Person', False)
        >>> ValidateBmi.is_valid('Normal')
        ('Normal', True)
        >>> ValidateBmi.is_valid('')
        ('INVALID', False)
        >>> ValidateBmi.is_valid('           ')
        ('INVALID', False)
        """
        result = False
        list_bmi = ['Obesity', 'Overweight', 'Normal', 'Underweight']
        g = to_check
        g = Wa.wash_all_but_string_characters(g)
        g = Wa.set_case(g)
        if g == '':
            g = "INVALID"
        if g == 'Obese':
            g = 'Obesity'
        if Va.is_in_list(g, list_bmi):
            result = True
        return g, result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
