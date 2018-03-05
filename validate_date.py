from datetime import datetime

import validator
import washer
import re

class ValidateDate(object):

    valid_date = ""

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
            datetime.strptime(data, date_format)
            result = True
        except ValueError:
            result = False

        return result

    def determine_month_format(self, data):
        # default to number format like 09 for September
        result = "%m"

        date_to_check = washer.Washer.replace_x_with_y("\W+", "/", data)
        split_date = self.split_string("/", date_to_check)
        for value in split_date:
            if value.isalpha():
                if len(value) > 3:
                    result = "%B"
                else:
                    result = "%b"

        return result

    def month_string_to_number(self, data):

        date_to_check = washer.Washer.replace_x_with_y("\W+", "/", data)
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

    def wash_data(self, data_to_wash):
        # replace any non-word character with a forward slash
        data_to_wash =  washer.Washer.replace_x_with_y("\W+", "/", data_to_wash)
        # remove st, nd and rd from date, e.g. 21st, 22nd, 23rd
        data_to_wash =  washer.Washer.replace_x_with_y("st|nd|rd", "", data_to_wash)

        data_to_wash = self.add_zeros(data_to_wash)

        washer.Washer.valid_date = data_to_wash

        return data_to_wash

    def is_valid(self, data_to_validate):
        result = False
        #date_format = '%d %m %Y'

        data_to_validate = self.wash_data(data_to_validate)

        # remove all spaces
        data_to_validate = data_to_validate.strip()

        #self.data = self.month_string_to_number(self.data)
        date_format = self.determine_date_format(data_to_validate)
        date_to_check = washer.Washer.replace_x_with_y('\W+', " ", data_to_validate)
        result = self.is_real_date(date_to_check, date_format)

        print(data_to_validate + " is valid: " + str(result))

        return result

i = ValidateDate()

result = i.is_valid("01-02-2020")
print(i.valid_date)
result = i.is_valid("32-02-2020")
print(i.valid_date)
result = i.is_valid("18-12-2018")
print(i.valid_date)
result = i.is_valid("03 February 2018")
print(i.valid_date)
result = i.is_valid("3rd Jan 2018")
print(i.valid_date)
result = i.is_valid("1st Jan 2018")
print(i.valid_date)
result = i.is_valid("2nd Jan 2018")
print(i.valid_date)
result = i.is_valid("1/1/1998")
print(i.valid_date)



print(datetime.strptime('Feb', '%b').month)
