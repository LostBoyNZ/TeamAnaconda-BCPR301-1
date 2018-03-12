# Graham

import datetime
import sys

try:
    #from validators.validator import Validator, is_correct_pattern, is_within_length, has_this_many_numbers, has_this_many_letters
    from validators.validator import Validator
except NameError and ModuleNotFoundError and ImportError:
     print("Fatal Error - validator.py not found.")
     sys.exit()

try:
    #from washer import Washer, replace_x_with_y, valid_date
    from washers.washer import Washer
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - washer.py not found.")
    sys.exit()


class ValidateDate():

    def split_string(self, delimiter, data):
        return data.split(delimiter)

    def add_zeros(self, data):
        split_date = self.split_string("/", data)
        day = split_date[0]
        month = split_date[1]
        year = split_date[2]

        if day.isdigit():
            day = day.zfill(2)
        if month.isdigit():
            month = month.zfill(2)

        return day + "/" + month + "/" + year

    def is_real_date(self, data, date_format):
        result = False

        try:
            datetime.datetime.strptime(data, date_format)
            result = True
        except ValueError:
            result = False

        return result

    def determine_month_format(self, data):
        # default to number format like 09 for September
        result = "%m"

        date_to_check = Washer.replace_x_with_y("\W+", "/", data)
        split_date = self.split_string("/", date_to_check)
        for value in split_date:
            if value.isalpha():
                if len(value) > 3:
                    result = "%B"
                else:
                    result = "%b"

        return result

    def month_string_to_number(self, data):

        date_to_check = Washer.replace_x_with_y("\W+", "/", data)
        split_date = self.split_string("/", date_to_check)
        for value in split_date:
            if value.isalpha():
                print("Is alpha")
                if len(value) > 3:
                    # result = "%B"
                    split_date[value] = datetime.strptime(value, '%B').month
                else:
                    # result = "%b"
                    split_date[value] = datetime.strptime(value, '%b').month

        return split_date[0] + "/" + split_date[1] + "/" + split_date[2]

    def determine_date_format(self, data):
        day_format = "%d"
        month_format = self.determine_month_format(data)
        #month_number = self.determine_month_format(data)
        year_format = "%Y"
        format = day_format + " " + month_format + " " + year_format
        #format = "%d %m %Y"

        return format

    @staticmethod
    def wash_data(data_to_wash):
        # replace any non-word character with a forward slash
        data_to_wash =  Washer.replace_x_with_y("\W+", "/", data_to_wash)
        # remove st, nd and rd from date, e.g. 21st, 22nd, 23rd
        data_to_wash =  Washer.replace_x_with_y("st|nd|rd", "", data_to_wash)

        return data_to_wash

    def is_valid(self, data_to_validate):
        result = False

        washed_data = self.wash_data(data_to_validate)

        # add zeros if needed
        washed_data = self.add_zeros(washed_data)
        # remove all spaces
        washed_data = washed_data.strip()

        date_format = self.determine_date_format(washed_data)
        date_to_check = Washer.replace_x_with_y('\W+', " ", washed_data)
        result = self.is_real_date(date_to_check, date_format)
        if result == True:
            date_output = Washer.replace_x_with_y(" ", "/", date_to_check)
        else:
            date_output = date_to_check

        return date_output, result

#
# Add some asserts like...
#
# if not condition:
#    raise AssertionError()
#