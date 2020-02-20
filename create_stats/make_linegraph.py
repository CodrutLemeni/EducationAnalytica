import matplotlib.pyplot as plt

marker_colors = ['blue', 'red', 'black']
line_colors = ['skyblue', 'coral', 'gray']
def make_linegraph(grades, years, title, export_path, x_label = 'Anul', y_label = 'Nota', limits = None, categories = None):
    years_label = []
    for year in years:
        years_label.append(int(year))
    for i, means in enumerate(grades):
        plt.plot(years_label,means,marker='o', markerfacecolor=marker_colors[i], markersize=8, color=line_colors[i], linewidth=2)
    axes = plt.gca()
    if limits is None:
        axes.set_ylim([5, 9])
    else:
        axes.set_ylim(limits)
    axes.set_xlim([2014,2020])
    plt.legend(categories, loc='upper left')
    plt.title(title)
    # plt.show()
    plt.savefig(export_path)
    plt.close()