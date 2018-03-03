import re

class Washer(object):
    #Graham
    # For example calling:
    #   keep_only_these_in_string("jun99", "a-z")
    # Returns:
    #   "jun"
    #
    # Because it only keeps letters a-z
    # a-zA-Z0-9 would keep all letters and numbers
    def keep_only_these_in_string(self, data, regex_to_keep):
        regex_target = re.compile(r"[^" + regex_to_keep + "]")

        data = regex_target.sub("", data)
        return data

    # Graham
    # Output will have one capital letter then all lowercase
    # e.g. tEsT would become Test
    def set_case(self, data):
        washed_data = data.title()

        return washed_data

    # Graham
    # For example calling:
    #   replace_x_with_y("-", "/")
    # Would change 10-01-1998 to 10/01/1998
    def replace_x_with_y(self, x, y, data):
        target = x
        replacement = y

        new_data = re.sub(target, replacement, data)

        return new_data
