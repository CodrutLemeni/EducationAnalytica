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
    ax.set_title("BAC 2018 specialisation comparison")
    plt.show()

def return_grades_as_array(l1, l2, l3):
        mate, filo, stiinte = [], [], []
        for x in l1:
            mate.append(x.final_grade)
        for x in l2:
            filo.append(x.final_grade)
        for x in l3:
            stiinte.append(x.final_grade)
        return mate, filo, stiinte


if __name__ == "__main__":
    csv_file = r'C:\Users\Patronu\BAC_2019_statistics\results.csv'
    all_students = initialiaze_students(csv_file)
    all_students = filter_by_grade(all_students, 5.0)

    mate_info_students = filter_by_specialisation(all_students, 'Â MATEMATICA-INFORMATICA' )
    filo_students = filter_by_specialisation(all_students, 'Â FILOLOGIE' )
    stiinte_students = filter_by_specialisation(all_students, 'Â STIINTE ALE NATURII' )

    mate, filo, stiinte = return_grades_as_array(mate_info_students, filo_students, stiinte_students)

    box_for_spec([mate,filo,stiinte])
