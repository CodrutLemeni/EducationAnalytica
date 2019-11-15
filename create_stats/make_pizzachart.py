import matplotlib.pyplot as plt
def make_pizzachart(numbers, labels, title, export_path):
    plt.pie(numbers, autopct='%1.1f%%', shadow = True, startangle = 140, radius = 1.9)
    plt.legend(labels)
    plt.axis('equal')
    plt.title(title)
    plt.savefig(export_path)

    # plt.show()