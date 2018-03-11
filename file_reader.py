import errors


class FileReader(object):  # Claye

    dict_root = {'': {}}

    def __init__(self):
        pass

    def split_file(self, file_name): # Claye
        file = open(file_name, "r")
        # Repeat for each line in the text file
        f = FileReader()
        for line in file:
            # Split the file into different fields using "," to split fields
            fields = line.split(",")
            y = fields[0]
            f.dict_root.update({y: {'gender': fields[1], 'age': fields[2], 'sales': fields[3], 'bmi': fields[4], 'salary': fields[5], 'birthday': fields[6]}})

        # print(f.dict_root['T456']['birthday'])
        # print(f.dict_root.keys())

        for key in f.dict_root:
            print([key])
            for value in f.dict_root[key]:
                print(f.dict_root[key][value])

        # Close the file to free up resources (good practice)
        file.close()

    @staticmethod
    def call_file():
        y = input("Please enter the filename: ")
        try:
            i.split_file(y)
        except FileNotFoundError:
            print(errors.ErrorHandler.get_error_message(201))

    def write_file(self):
        u = input("Are you sure you want to save data? Y/N > ")
        if u.upper() == "Y":
            f = FileReader()
            z = open("data.txt", "a")
            for key in f.dict_root:
                z.write(str([key]) + '\n')
                for value in f.dict_root[key]:
                    h = str(f.dict_root[key][value])
                    z.write(value + ' ' + h)
                    z.write("\n")
            z.close()
            print("File saved")
        elif u.upper() == "N":
            print("Data Not saved")
        else:
            print(errors.ErrorHandler.get_error_message(102))
            self.write_file()


i = FileReader()
i.call_file()
i.write_file()
