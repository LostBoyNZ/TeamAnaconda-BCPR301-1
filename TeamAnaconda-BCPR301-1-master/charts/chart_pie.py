# Graham
import sys

try:
    from errors import ErrorHandler as err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError and ImportError:
    print("matplotlib.pyplot not avaliable")
    sys.exit()


class ChartPie(object): # Graham

    def create_pie_chart(self, data, data_type):
        chart_data = ""
        if data_type == "gender":
            data_labels, title, window_title = self._gender(data)
            chart_data = data_type
        elif data_type == "sales":
            data_labels, title, window_title = self._sales(data)
            chart_data = data_type
        else:
            # This type of data isn't supported in a pie chart
            print(err.get_error_message(601))

        if chart_data:
            sizes = data
            labels = data_labels
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')
            ax1.set_title(title)
            fig = plt.gcf()
            fig.canvas.set_window_title(window_title)

            plt.show()

    def _gender(self, data):
        data_labels = "Female", "Male"
        title = "Gender"
        window_title = "Gender Pie Graph"

        return data_labels, title, window_title

    def _sales(self, data):
        data_labels = "< 250", "250 - 499", "500 - 749", "750 - 999"
        title = "Sales Brackets"
        window_title = "Sales Brackets"

        return data_labels, title, window_title