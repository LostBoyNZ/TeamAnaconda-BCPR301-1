import errors
from data_processor import DataProcessor
import os.path


class FileReader(object):  # Claye

    dict_root = {}

    def call_file(self):
        y = input("Please enter the filename to read data from >>> ")
        try:
            self.split_file(y)
        except FileNotFoundError:
            print(errors.ErrorHandler.get_error_message(201))

    def split_file(self, file_name): # Claye
        file = open(file_name, "r")
        # Repeat for each line in the text file
        f = FileReader()
        for line in file:
            # Split the file into different fields using "," to split fields
            fields = line.split(",")
            f.dict_root.update({fields[0]: {'gender': fields[1], 'age': fields[2], 'sales': fields[3], 'bmi': fields[4], 'salary': fields[5], 'birthday': fields[6].rstrip(), 'valid': '0'}})
        # Close the file to free up resources (good practice)
        file.close()
        valid_dict = DataProcessor.send_to_validate(f.dict_root)
        self.write_file(valid_dict)

    def write_file(self, dict_valid):
        u = input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            file_target = input("Please input the filename to save to >>> ")
            if os.path.exists("{}".format(file_target)):
                u2 = input("File exists, do you want to append the data Y/N >>> ")
                if u2.upper() == 'Y':
                    self.commit_save(dict_valid, file_target)
                if u2.upper() == 'N':
                    self.write_file(dict_valid)
            else:
                self.commit_save(dict_valid, file_target)
        elif u.upper() == "N":
            print("Data Not saved")
        else:
            print(errors.ErrorHandler.get_error_message(102))
            self.write_file(dict_valid)

    def commit_save(self, dict_valid, file_target):
            z = open(file_target, "a")
            for key in dict_valid:
                z.write("\n")
                z.write(key + ",")
                for value in dict_valid[key]:
                    h = str(dict_valid[key][value] + ",")
                    z.write(value + ' ' + h)
            z.write("\n")
            z.close()
            print("File saved")

# i = FileReader()
# i.call_file()
