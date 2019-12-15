import matplotlib.pyplot as plt
def make_pizzachart(numbers, labels, title, export_path):
    plt.pie(numbers, autopct='%1.1f%%', startangle = 180, radius = 1.4)
    plt.axis('equal')
    plt.title(title)
    plt.legend(labels)
    figure=plt.gcf()
    figure.set_size_inches(18.6,9.8)
    plt.savefig(export_path)
    plt.close()