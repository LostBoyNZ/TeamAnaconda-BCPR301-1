import re

class Washer(object):
    #Graham
    def keep_only_letters_numbers(self, data):
        characters_to_keep = re.compile(r"[^a-zA-Z0-9]")
        washed_data = characters_to_keep.sub("", data)

        return washed_data

    # Graham
    def set_case(self, data):
        washed_data = data.title()

        return washed_data

    # Graham
    def replace_x_with_y(self, x, y):
        target = x
        replacement = y

        self.data = re.sub(target, replacement, self.data)
