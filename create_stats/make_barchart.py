import numpy as np
import matplotlib.pyplot as plt 

def make_barchart_percentage(all_categories, all_categories_good, categories_names, title, current_export_path, colors):

    percentage = []
    for i in range(len(all_categories)):
        percentage.append(float(len(all_categories_good[i])) / float(len(all_categories[i])) * 100)
    
    
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

        value = str(round(percentage[i], 2)) + '%'
        # Shift the text to the left side of the right edge
        xloc = -5
        # White on magenta
        clr = '#010a43'
        align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height() / 2
        label = ax.annotate(str(len(all_categories_good[i])) + " - " + value, xy=(width, yloc), xytext=(xloc, 0),
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

def make_barchart_percentage_subject3(all_students, all_grades, categories_names, title, current_export_path, colors):

    total_students = 0
    for students in all_students:
        total_students += len(students)

    percentage = []

    for i in range(len(all_students)):
        percentage.append(float(len(all_students[i])) / float(total_students) * 100)
    
    
    plt.rcdefaults()
    fig,ax = plt.subplots()
    y_pos = np.arange(len(all_students))

    rects = ax.barh(y_pos, percentage, align='center', color=colors)
    
    i = 0
    for rect in rects:
        width = int(rect.get_width())

        value = str(round(percentage[i], 2)) + '%'
        xloc = -5

        if width < 19:
            # Shift the text to the right side of the right edge
            xloc = 5
            # Black against white background
            clr = '#010a43'
            align = 'left'
        else:
            # Shift the text to the left side of the right edge
            xloc = -5
            # White on magenta
            clr = '#010a43'
            align = 'right'

        yloc = rect.get_y() + rect.get_height() / 2
        label = ax.annotate(str(len(all_students[i])) + " - " + value + " - Media:" + str(round(all_grades[i], 2)), xy=(width, yloc), xytext=(xloc, 0),
                            textcoords="offset points",
                            ha=align, va='center',
                            color=clr, weight='bold', clip_on=True)
        i = i + 1
    

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories_names)
    ax.set_xlabel('Procentaj')
    

    ax.set_title(title)

    plt.savefig(current_export_path)

def make_barchart_values(all_categories, categories_names, title, current_export_path, colors):
    
    
    plt.rcdefaults()
    fig,ax = plt.subplots()
    y_pos = np.arange(len(all_categories))

    rects = ax.barh(y_pos, all_categories, align='center', color=colors)
    i = 0
    for rect in rects:
        # Rectangle widths are already integer-valued but are floating
        # type, so it helps to remove the trailing decimal point and 0 by
        # converting width to int type
        width = int(rect.get_width())

        value = all_categories[i]
        # Shift the text to the left side of the right edge
        xloc = -5
        # White on magenta
        clr = '#010a43'
        align = 'right'

        # Center the text vertically in the bar
        yloc = rect.get_y() + rect.get_height() / 2
        label = ax.annotate(str(round(value, 2)), xy=(width, yloc), xytext=(xloc, 0),
                            textcoords="offset points",
                            ha=align, va='center',
                            color=clr, weight='bold', clip_on=True)
        i = i + 1

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories_names)
    ax.set_xlabel('Nota')
    

    ax.set_title(title)
    #ax.annotate

    plt.savefig(current_export_path)
    

     