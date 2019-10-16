import numpy as np
import matplotlib.pyplot as plt 

def make_boxplot(grades, labels, medium=None):
    '''
        Plotting boxplots for 3 specialisations
    '''
    colors = ['cyan', 'lightblue'] * 3;

    grades = np.array(grades)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    box = ax.boxplot(grades, notch=True, patch_artist=True)
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    ax.set_xticklabels(['MATE_INFO', 'FILO', 'STIINTE'])
    ax.set_xticks([1.5, 3.5, 5.5])
    ax.set_ylabel("NOTE")
    ax.set_xlabel("SPECIALIZARE")
    env = '' if medium == None else '- ' + medium
    ax.set_title(f"BAC 2019 specialisation comparison {env}")
    ax.legend([ box['boxes'][0], box['boxes'][1] ], ['Baieti', 'Fete'], loc='upper right')
    plt.show()