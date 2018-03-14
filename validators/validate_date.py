# Graham

from datetime import datetime
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
        try:
            split_date = self.split_string("/", data)
            day = split_date[0]
            month = split_date[1]
            year = split_date[2]

            if day.isdigit():
                day = day.zfill(2)
            if month.isdigit():
                month = month.zfill(2)

            output = day + "/" + month + "/" + year
        except IndexError:
            output = data

        return output

    def is_real_date(self, data, date_format):
        result = False

        try:
            datetime.strptime(data, date_format)
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
                print(value)
                if len(value) > 3:
                    # result = "%B"
                    text_month = datetime.strptime(value, '%B')
                    split_date[1] = text_month.strftime('%m')
                else:
                    # result = "%b"
                    text_month = datetime.strptime(value, '%b')
                    split_date[1] = text_month.strftime('%m')

        return split_date[0] + "/" + split_date[1] + "/" + split_date[2]

    def determine_date_format(self, data):
        day_format = "%d"
        month_format = self.determine_month_format(data)
        #month_number = self.determine_month_format(data)
        year_format = "%Y"
        format = day_format + " " + month_format + " " + year_format
        #format = "%d %m %Y"

        return format

    def wash_data(self, data_to_wash):
        # replace any non-word character with a forward slash
        data_to_wash =  Washer.replace_x_with_y("\W+", "/", data_to_wash)
        # remove st, nd and rd from date, e.g. 21st, 22nd, 23rd
        data_to_wash =  Washer.replace_x_with_y("st|nd|rd", "", data_to_wash)
        data_to_wash = self.month_string_to_number(data_to_wash)

        return data_to_wash

    def is_valid(self, data_to_validate):
        result = False

        data_to_validate = data_to_validate.lstrip(' ')

        # If there's no numbers in the string, just return string as is, it's bad data
        if Validator.has_this_many_numbers(0, data_to_validate):
            date_output = data_to_validate
        else:
            washed_data = self.wash_data(data_to_validate)

            # add zeros if needed
            washed_data = self.add_zeros(washed_data)

            # remove all spaces
            washed_data = washed_data.strip()

            date_format = self.determine_date_format(washed_data)
            date_to_check = Washer.replace_x_with_y('\W+', " ", washed_data)
            result = self.is_real_date(date_to_check, date_format)

            date_output = Washer.replace_x_with_y(" ", "/", date_to_check)

        return date_output, result
