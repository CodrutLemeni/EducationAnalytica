import numpy as np
import matplotlib.pyplot as plt 

def make_barchart_percentage(all_categories, categories_names, title, current_export_path, colors):
    all_categories_no = 0
    for category in all_categories:
        all_categories_no += len(category)
    percentage = []
    for category in all_categories:
        percentage.append(float(len(category)) / all_categories_no * 100)
    
    plt.rcdefaults()
    fig,ax = plt.subplots()
    y_pos = np.arange(len(all_categories))

    rects = ax.barh(y_pos, percentage, align='center', color=colors)
    i = 0
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating
        # type, so it helps to remove the trailing decimal point and 0 by
        # converting width to int type
        width = int(rect.get_width())

        value = percentage[i]
        # Shift the text to the left side of the right edge
        xloc = -5
        # White on magenta
        clr = '#010a43'
        align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height() / 2
        label = ax.annotate(str(round(value, 2)) + '%', xy=(width, yloc), xytext=(xloc, 0),
                            textcoords="offset points",
                            ha=align, va='center',
                            color=clr, weight='bold', clip_on=True)
        i = i + 1

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories_names)
    ax.set_xlabel('Procentaj')
    

    ax.set_title(title)
    #ax.annotate

    plt.savefig(current_export_path)
    

     