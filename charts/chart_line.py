import matplotlib.pyplot as plt


class ChartLine:

    @staticmethod
    def create_line_grid(a_list, s_list):
        plt.title('Salary Vs Age')
        plt.grid(True)
        plt.plot(a_list[0:], s_list[0:])
        plt.ylabel('salary')
        plt.xlabel('age')
        plt.show()

    def sort_line_grid_data(self, x_axis_data, y_axis_data):
        print("func reached")
