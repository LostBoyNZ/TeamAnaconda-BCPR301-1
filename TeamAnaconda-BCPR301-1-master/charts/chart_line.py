import matplotlib.pyplot as plt


class ChartLine:

    @staticmethod
    def create_line_grid(age_list, salary_list):
        salary_list = [int(i) for i in salary_list]
        age_list = [int(i) for i in age_list]
        age_list, salary_list = zip(*sorted(zip(age_list, salary_list)))
        plt.plot(age_list[0:], salary_list[0:])
        plt.title('Salary Vs Age')
        plt.ylabel('Salary')
        plt.xlabel('Age')
        plt.grid(True)
        fig = plt.gcf()
        fig.canvas.set_window_title('Salary Vs Age')
        plt.show()
