# Rochelle
import numpy as np
import matplotlib.pyplot as plt


class ChartBar(object):

    def create_bar_chart(self, title, ylabel, objects, data):
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, data, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel(ylabel)
        plt.title(title)

        plt.show()
