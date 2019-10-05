import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, r"C:\Users\Patronu\BAC_2019_statistics\classes")
import pandas as pd
import numpy as np
from student import *

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
    ax.set_title("BOXPLOT")
    plt.show()


if __name__ == "__main__":
    csv_file = r'C:\Users\Patronu\BAC_2019_statistics\results.csv'
    all_students = initialiaze_students(csv_file)
    all_students = filter_by_grade(all_students)

    mate_info_students = filter_by_specialisation(all_students, 'Â MATEMATICA-INFORMATICA' )
    filo_students = filter_by_specialisation(all_students, 'Â FILOLOGIE' )
    stiinte_students = filter_by_specialisation(all_students, 'Â STIINTE ALE NATURII' )

    mate, filo, stiinte = [], [], []
    for x in mate_info_students:
        mate.append(x.final_grade)
    for x in filo_students:
        filo.append(x.final_grade)
    for x in stiinte_students:
        stiinte.append(x.final_grade)

    box_for_spec([mate,filo,stiinte])
