# Rochelle
import numpy as np
import matplotlib.pyplot as plt


class ChartBMI(object):

    def __init__(self, n, ov, ob, u):
        self.normal = n
        self.overweight = ov
        self.obesity = ob
        self.underweight = u
        self.bmi = [n, ov, ob, u]

    def make_chart(self):
        objects = ('Normal', 'Overweight', 'Obesity', 'Underweight')
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, self.bmi, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number')
        plt.title('BMI')

        plt.show()


weights = [40, 20, 12, 7]
normal = 40
overweight = 20
obesity = 12
underweight = 7
i = ChartBMI(normal, overweight, obesity, underweight)
i.make_chart()


