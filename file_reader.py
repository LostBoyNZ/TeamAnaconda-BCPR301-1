import errors
from data_processor import DataProcessor


class FileReader(object):  # Claye

    dict_root = {'': {}}

    def __init__(self):
        pass

    def call_file(self):
        y = input("Please enter the filename: ")
        try:
            self.split_file(y)
        except FileNotFoundError:
            print(errors.ErrorHandler.get_error_message(201))

    def split_file(self, file_name): # Claye
        file = open(file_name, "r")
        # Repeat for each line in the text file
        f = FileReader()
        del f.dict_root['']
        for line in file:
            # Split the file into different fields using "," to split fields
            fields = line.split(",")
            f.dict_root.update({ fields[0]: {'gender': fields[1], 'age': fields[2], 'sales': fields[3], 'bmi': fields[4], 'salary': fields[5], 'birthday': fields[6].rstrip()}})
        # Close the file to free up resources (good practice)
        file.close()
        valid_dict = DataProcessor.send_to_validate(f.dict_root)
        self.write_file(valid_dict)

    def write_file(self, dict_valid):
        u = input("Are you sure you want to save data? Y/N > ")
        if u.upper() == "Y":
            z = open("data.txt", "a")
            for key in dict_valid:
                z.write("\n")
                z.write(key + ",")
                for value in dict_valid[key]:
                    h = str(dict_valid[key][value] + ",")
                    z.write(value + ' ' + h)
            z.write("\n")
            z.close()
            print("File saved")
        elif u.upper() == "N":
            print("Data Not saved")
        else:
            print(errors.ErrorHandler.get_error_message(102))
            self.write_file()


# i = FileReader()
# i.call_file()
