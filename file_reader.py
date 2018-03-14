import errors
from data_processor import DataProcessor
from log_file_handler import LogFileHandler
from openpyxl import load_workbook
import os.path
import sys

# from database_excel import DatabaseExcel as dbexcel

try:
    from database_excel import DatabaseExcel as dbexel
except NameError and ModuleNotFoundError and ImportError:
    print(errors.get_error_message(404, "database_excel"))
    sys.exit()


class FileReader(object):  # Claye

    def call_file(self, switch):
        file_name = input("Please enter the filename to read data from >>> ")
        split_filename = file_name.split(".")
        file_extension = split_filename[-1]
        if file_extension == "xls" or file_extension == "xlsx":
            try:
                wb = load_workbook(file_name)
            except FileNotFoundError:
                print(errors.get_error_message(201))
                self.call_file(switch)
            except OSError:
                print(errors.get_error_message(103))
                self.call_file(switch)

            i = dbexel()
            data_to_save = i.create_connection(wb, switch)
            self.write_file(data_to_save)
        elif file_extension == "txt" or file_extension == "csv":
            try:
                self.split_file(file_name, switch)
            except FileNotFoundError:
                print(errors.ErrorHandler.get_error_message(201))
                self.call_file(switch)
            except OSError:
                print(errors.ErrorHandler.get_error_message(103))
                self.call_file(switch)
        else:
            print(errors.ErrorHandler.get_error_message(204))

    def split_file(self, file_name, switch): # Claye, Works with CSV and TXT docs
        dict_root = {}
        file = open(file_name, "r")
        # Repeat for each line in the text file
        f = FileReader()
        dup_keys = 0
        for line in file:
            # Split the file into different fields using "," to split fields
            fields = line.split(",")
            checked_id = DataProcessor.validate_key(fields[0])
            if checked_id in dict_root:
                dup_keys += 1
                fields[6] = fields[6].rstrip()
                data_to_log = "Duplicate Key" + str(fields[0:])
                LogFileHandler.append_file('log.txt', data_to_log)
            else:
                dict_root.update({checked_id: {'gender': fields[1], 'age': fields[2], 'sales': fields[3], 'bmi': fields[4], 'salary': fields[5], 'birthday': fields[6].rstrip(), 'valid': '0'}})
        # Close the file to free up resources (good practice)
        file.close()
        valid_dict = DataProcessor.send_to_validate(dict_root, switch, dup_keys)
        self.write_file(valid_dict)

    def write_file(self, dict_valid):
        u = input("Are you sure you want to save data? Y/N >>> ")
        if u.upper() == "Y":
            file_target = input("Please input the filename to save to >>> ")
            if self.check_path_exists(file_target):
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
        try:
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
        except OSError:
            print(errors.ErrorHandler.get_error_message(103))
            self.write_file(dict_valid)


    @staticmethod
    def check_path_exists(path):
        result = False
        try:
            if os.path.exists("{}".format(path)):
                result = True
                return result
            else:
                return result
        except OSError:
            print(errors.ErrorHandler.get_error_message(103))

# i = FileReader()
# i.call_file()