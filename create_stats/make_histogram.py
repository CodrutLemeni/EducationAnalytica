import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

def make_histogram( grades, colors, x_label='Note', y_label='Procentaj', title='BAC',legend=['Baieti','Fete']):
    
    plt.hist( grades, color=colors, bins=5, rwidth=1 )
    # plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.legend(legend)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.xticks(range(5,11))
    plt.yticks(range(0,40,5))
    # plt.hist( [boys_grades,girls_grades], 5)

    plt.show()