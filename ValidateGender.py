import re

class ValidateAge(object):

    def __init__(self, gender):
        self.gender = gender

    def is_valid(self):
        gender_list = ['M', 'F' 'Boy', 'Girl', 'Male', 'Female', 'Dude', 'Lady']
        g = self.gender
        g = self.wash_data(g)

        if any(g in s for s in gender_list):
            result = True
        else:
            result = False
        print(g)
        return result

    @staticmethod
    def wash_data(to_wash):
        to_wash = ''.join([c for c in to_wash if c not in " 1234567890"])
        to_wash = re.sub(r'[^\w]', '', to_wash)
        to_wash = to_wash.title()

        return to_wash





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

