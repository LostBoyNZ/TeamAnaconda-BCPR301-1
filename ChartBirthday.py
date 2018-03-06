# Rochelle
import numpy as np
import matplotlib.pyplot as plt


class ChartBirthday(object):

    def __init__(self, months):
        self.months = months

    def make_chart(self):
        objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, self.months, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number')
        plt.title('Birth Months')

        plt.show()


months1 = [3, 2, 7, 6, 5, 2, 1, 10, 4, 9, 6, 3]

i = ChartBirthday(months1)
i.make_chart()
