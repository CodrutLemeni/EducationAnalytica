import matplotlib.pyplot as plt

def make_linegraph(grades, years, title, x_label = 'Anul', y_label = 'Nota',
                   first_category = "Baieti", second_category = "Fete"):
    years_label = []
    for year in years:
        years_label.append(int(year))
    plt.plot(years_label,grades[0],marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
    plt.plot(years_label,grades[1],marker='o', markerfacecolor='red', markersize=8, color='coral', linewidth=2)
    axes = plt.gca()
    axes.set_ylim([5, 8])
    axes.set_xlim([2014,2020])
    plt.legend([first_category, second_category], loc='upper left')
    plt.title(title)
    plt.show()