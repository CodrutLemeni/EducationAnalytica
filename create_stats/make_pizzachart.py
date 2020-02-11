import matplotlib.pyplot as plt
import os

def make_pizzachart(numbers, labels, title, export_path):
    plt.close()
    plt.pie(numbers, autopct='%1.1f%%', startangle = 180, radius = 1.4)
    plt.axis('equal')
    plt.title(title)
    plt.legend(labels)
    figure=plt.gcf()
    figure.set_size_inches(18.6,9.8)
    plt.savefig(os.path.join(export_path,title))
    plt.close(figure)
    plt.close()