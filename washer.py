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
    @staticmethod
    def keep_only_these_in_string(regex_to_keep, data):
        regex_target = re.compile(r"[^" + regex_to_keep + "]")

        new_data = regex_target.sub("", data)
        return new_data

    # Graham
    # Output will have one capital letter then all lowercase
    # e.g. tEsT would become Test
    @staticmethod
    def set_case(data):
        new_data = data.title()

        return new_data

    # Graham
    # For example calling:
    #   replace_x_with_y("-", "/")
    # Would change 10-01-1998 to 10/01/1998
    @staticmethod
    def replace_x_with_y(x, y, data):
        target = x
        replacement = y

        new_data = re.sub(target, replacement, data)

        return new_data
