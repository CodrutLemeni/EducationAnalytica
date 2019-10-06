import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append( r"D:\Work\bac_stats\stats_bac")

import pandas as pd
import numpy as np
from classes.student import *

def box_for_spec(grades, labels):
    '''
        Plotting boxplots for 3 specialisations
    '''
    grades = np.array(grades)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(grades, labels=labels)
    ax.set_ylabel("NOTE")
    ax.set_xlabel("SPECIALIZARE")
    ax.set_title("BAC 2019 specialisation comparison")
    plt.show()

def return_grades_as_array(specs):
        #mate, filo, stiinte = [], [], []
        grades = [ [] for i in range(len(specs)) ]
        for x in specs[0]:
            grades[0].append(x.final_grade)
        for x in specs[1]:
            grades[1].append(x.final_grade)
        for x in specs[2]:
            grades[2].append(x.final_grade)
        return grades


if __name__ == "__main__":
    csv_file = r'D:\Work\bac_stats\stats_bac\results_2019.csv'
    all_students = initialiaze_students(csv_file)
    all_students = filter_by_grade(all_students, 5.0)

    mate_info_students = filter_by_specialisation(all_students, 'Â MATEMATICA-INFORMATICA' )
    filo_students = filter_by_specialisation(all_students, 'Â FILOLOGIE' )
    stiinte_students = filter_by_specialisation(all_students, 'Â STIINTE ALE NATURII' )

    grades = return_grades_as_array([mate_info_students, filo_students, stiinte_students])

    box_for_spec(grades, ["MATE-INFO", "FILO", "STIINTE"])
