import sys
from charts.chart_line import ChartLine
from charts.chart_bar import ChartBar
# from charts.chart_pie import ChartPie

try:
    from errors import ErrorHandler as err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()


class CalcData(object):

    def __init__(self):
        self.count_gender_m = 0
        self.count_gender_f = 0
        self.count_bmi_ov = 0
        self.count_bmi_ob = 0
        self.count_bmi_un = 0
        self.count_bmi_no = 0
        self.count_sales_group1 = 0
        self.count_sales_group2 = 0
        self.count_sales_group3 = 0
        self.count_sales_group4 = 0
        self.count_birth_jan = 0
        self.count_birth_feb = 0
        self.count_birth_mar = 0
        self.count_birth_apr = 0
        self.count_birth_may = 0
        self.count_birth_jun = 0
        self.count_birth_jul = 0
        self.count_birth_aug = 0
        self.count_birth_sep = 0
        self.count_birth_oct = 0
        self.count_birth_nov = 0
        self.count_birth_dec = 0
        self.age_list = []
        self.salary_list = []

    def is_valid(self, file_contents):
        result = False
        values = ['gender', 'age', 'birthday', 'bmi', 'sales', 'salary']
        contents = ''.join(file_contents)
        count = 0
        for value in values:
            if value in contents:
                count += 1
        if count == len(values):
            result = True
        return result

    def calculate(self, file_contents):
        dict_data = {}
        for line in file_contents[1:]:
            fields = line.split(",")
            if 'valid 1' in fields:
                for item in fields[1:-1]:
                    items = item.split(" ")
                    dict = {items[0]: items[1]}
                    for key, value in dict.items():
                            if key == 'gender':
                                if value == 'M':
                                    self.count_gender_m += 1
                                if value == 'F':
                                    self.count_gender_f += 1
                            elif key == 'age':
                                self.age_list += [value]
                            elif key == 'sales':
                                if 0 <= int(value) >= 249:
                                    self.count_sales_group1 += 1
                                elif 250 <= int(value) >= 499:
                                    self.count_sales_group2 += 1
                                elif 500 <= int(value) >= 749:
                                    self.count_sales_group3 += 1
                                elif 750 <= int(value) >= 999:
                                    self.count_sales_group4 += 1
                            elif key == 'bmi':
                                if value == 'Overweight':
                                    self.count_bmi_ov += 1
                                elif value == 'Obesity':
                                    self.count_bmi_ob += 1
                                elif value == 'Underweight':
                                    self.count_bmi_un += 1
                                elif value == 'Normal':
                                    self.count_bmi_no += 1
                            elif key == 'salary':
                                self.salary_list += [value]
                            elif key == 'birthday':
                                month = value.split('/')[0]
                                if month == '01':
                                    self.count_birth_jan += 1
                                elif month == '02':
                                    self.count_birth_feb += 1
                                elif month == '03':
                                    self.count_birth_mar += 1
                                elif month == '04':
                                    self.count_birth_apr += 1
                                elif month == '05':
                                    self.count_birth_may += 1
                                elif month == '06':
                                    self.count_birth_jun += 1
                                elif month == '07':
                                    self.count_birth_jul += 1
                                elif month == '08':
                                    self.count_birth_aug += 1
                                elif month == '09':
                                    self.count_birth_sep += 1
                                elif month == '10':
                                    self.count_birth_oct += 1
                                elif month == '11':
                                    self.count_birth_nov += 1
                                elif month == '12':
                                    self.count_birth_dec += 1

    def line_chart(self):
        i = ChartLine()
        i.create_line_grid(self.age_list, self.salary_list)

    def bar_chart(self, choice):
        i = ChartBar()
        if choice == 'bmi':
            title = 'BMI'
            ylabel = 'Number'
            objects = ('Normal', 'Overweight', 'Obesity', 'Underweight')
            data = [self.count_bmi_ov, self.count_bmi_ob, self.count_bmi_un, self.count_bmi_no]
            i.create_bar_chart(title, ylabel, objects, data)
        elif choice == 'birthday':
            title = 'Birth Months'
            ylabel = 'Number'
            objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
            data = [self.count_birth_jan, self.count_birth_feb, self.count_birth_mar, self.count_birth_apr, self.count_birth_may, self.count_birth_jun,
                    self.count_birth_jul, self.count_birth_aug, self.count_birth_sep, self.count_birth_oct, self.count_birth_nov, self.count_birth_dec]
            i.create_bar_chart(title, ylabel, objects, data)

    def pie_chart(self, choice):
        # i = ChartPie()
        if choice == 'sales':
            data = [self.count_sales_group1, self.count_sales_group2, self.count_sales_group3, self.count_sales_group4]
            # i.create_pie_chart(data)
        elif choice == 'gender':
            data = [self.count_gender_f, self.count_gender_m]
            # i.create_pie_chart(data)
