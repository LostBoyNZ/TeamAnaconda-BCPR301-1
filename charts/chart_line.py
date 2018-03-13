import matplotlib.pyplot as plt


class ChartLine:

    @staticmethod
    def create_line_grid(a_list, s_list):
        s_list = [int(i) for i in s_list]
        a_list = [int(i) for i in a_list]
        a_list, s_list = zip(*sorted(zip(a_list, s_list)))
        plt.title('Salary Vs Age')
        plt.grid(True)
        plt.plot(a_list[0:], s_list[0:])
        plt.ylabel('Salary')
        plt.xlabel('Age')
        plt.show()


