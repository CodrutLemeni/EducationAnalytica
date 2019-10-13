import sys
sys.path.append(r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics')
import numpy as np
import matplotlib.pyplot as plt


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

if __name__ == "__main__":
    csv_file = r'/home/sebastian/Dropbox/Facultate/BacStats/good_bac_2019.csv'
    all_students = initialiaze_students(csv_file)
    all_students = filter_by_grade(all_students, 5.0)

    mate_info_students = filter_by_specialisation(all_students, 'matematica-informatica' )
    filo_students = filter_by_specialisation(all_students, 'filologie' )
    stiinte_students = filter_by_specialisation(all_students, 'stiinte ale naturii' )



    grades = return_grades_as_array([mate_info_students, filo_students, stiinte_students])

    box_for_spec(grades, ["MATE-INFO", "FILO", "STIINTE"])
