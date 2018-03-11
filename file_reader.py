import errors
from data_processor import DataProcessor
from validators.validate_gender import ValidateGender as vg
from validators.validate_bmi import ValidateBmi as vb
from validators.validate_date import ValidateDate as vd
from validators.validate_empid import ValidateEmpid as ve


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
            f.dict_root.update({ fields[0]: {'gender': fields[1], 'age': fields[2], 'sales': fields[3], 'bmi': fields[4], 'salary': fields[5], 'birthday': fields[6].rstrip()}})
        # Close the file to free up resources (good practice)
        file.close()
        self.send_to_validate()

    def send_to_validate(self):
        for k, v in self.dict_root.items():
            if k != '':
                print("EMPID")
                result = ve.is_valid(k)
                print(result)
                for kv in v.keys():
                    if kv == 'gender':
                        print("GENDER")
                        result = vg.is_valid(vg, self.dict_root[k][kv])
                        print(result)
                    if kv == 'bmi':
                        print("BMI")
                        result = vb.is_valid(vb, self.dict_root[k][kv])
                        print(result)
                    # if kv == 'birthday':
                    #     print("BIRTHDAY")
                    #     print(self.dict_root[k][kv])
                    #     result = vd.is_valid(vd, self.dict_root[k][kv])
                    #     print(result)

                # print(self.dict_root[z][o])

    # def send_to_validate(self):
    #     for k, v in self.dict_root.items():
    #         o = 'gender'
    #         print(v.keys())
    #         # print(x)
    #         if k != '':
    #             print(v['gender'])
    #             print(self.dict_root[k][o])
    #         # print(self.dict_root[z][o])

    def call_file(self):
        y = input("Please enter the filename: ")
        try:
            self.split_file(y)
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
# i.write_file()
