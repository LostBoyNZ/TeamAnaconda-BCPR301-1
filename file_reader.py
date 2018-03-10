import errors


class FileReader(object):  # Claye

    empid, gender, age, sales, bmi, salary, birthday = ([], [], [], [], [], [], [])

    def __init__(self):
        pass

    def split_file(self, file_name): # Claye
        file = open(file_name, "r")
        # Repeat for each line in the text file
        f = FileReader()
        x = 0
        for line in file:
            # Split the file into different fields using "," to split fields
            fields = line.split(",")

            # Sets the split data into individual lists
            f.empid.append(fields[0])
            f.gender.append(fields[1])
            f.age.append(fields[2])
            f.sales.append(fields[3])
            f.bmi.append(fields[4])
            f.salary.append(fields[5])
            f.birthday.append(fields[6])

            # Print the file
            print("{0} {1}".format("EMPID: ", f.empid[x]) + " Gender: " + f.gender[x] + " Age: " + f.age[x] + " Sales: " + f.sales[x] + " BMI: "
                  + f.bmi[x] + " Salary: " + f.salary[x] + " Birthday: " + f.birthday[x])
            x += 1

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
            x = 0
            f = FileReader()
            z = open("data.txt", "a")
            for entry in f.empid:
                z.write(f.empid[x] + " | " + f.gender[x] + " | " + f.age[x] + " | " + f.salary[x] + " | " + f.bmi[x] + " , " + f.salary[x] + " , " + f.birthday[x])
                x += 1
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
