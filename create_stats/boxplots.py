import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

f1 = r"mate_info.txt"
f2 = r"filologie.txt"
f3 = r"stiinte_naturii.txt"

def read_data(f1):
    '''
        Reads grades from file
    '''
    fin = open(f1)
    inp = fin.read()
    inp = inp.split('\n')

    grades = []
    specs = []

    for gr in inp:
        gr = gr.split(' ')
        if len( gr ) > 1 : grades.append( float(gr[1]) )

    return grades

def box_for_spec(grades):
    '''
        Plotting boxplots for 3 specialisations
    '''
    grades = np.array(grades)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(grades, labels = ["MATE-INFO", "FILO", "STIINTE"])
    ax.set_ylabel("NOTE")
    ax.set_xlabel("SPECIALIZARE")
    plt.show()


if __name__ == "__main__":
    note1 = read_data(f1)
    note2 = read_data(f2)
    note3 = read_data(f3)
    box_for_spec([note1, note2, note3])
