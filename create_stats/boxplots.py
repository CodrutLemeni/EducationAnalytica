import sys
sys.path.append(r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics')
import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
=======
sys.path.append( r"../" )

>>>>>>> master

import numpy as np
from classes.student import *
from classes.highschool import *
from  create_stats.make_boxplot import *

<<<<<<< HEAD
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

=======
def box_for_spec(all_students, medium=None):
>>>>>>> master
    mate_info_students = filter_by_specialisation(all_students, 'matematica-informatica' )
    filo_students = filter_by_specialisation(all_students, 'filologie' )
    stiinte_students = filter_by_specialisation(all_students, 'stiinte ale naturii' )

    mate_info_boys = filter_by_gender(mate_info_students, "M")
    filo_boys = filter_by_gender(filo_students, "M")
    stiinte_boys = filter_by_gender(stiinte_students, "M")

    mate_info_girls = filter_by_gender(mate_info_students, "F")
    filo_girls = filter_by_gender(filo_students, "F")
    stiinte_girls = filter_by_gender(stiinte_students, "F")

    grades = return_grades_as_array([mate_info_boys, mate_info_girls,
                                    filo_boys, filo_girls,
                                    stiinte_boys, stiinte_girls])

    make_boxplot(grades, ["MATE-INFO", "FILO", "STIINTE"], medium)


if __name__ == "__main__":
    csv_file = r'/home/cosmi/Desktop/BAC_stats/BAC_2019_statistics/data/2019/good_bac_2019.csv'
    schools_csv_file = r'/home/cosmi/Desktop/BAC_stats/BAC_2019_statistics/data/2019/unitati_scolare_2019.csv'
    all_students = initialiaze_students(csv_file, schools_csv_file)
    all_students = filter_by_grade(all_students, 5.0)

    box_for_spec(all_students)
    medium = "urban"
    #medium = "rural"
    students = filter_by_medium( all_students, medium) # second parameter can be "rural" or "urban"
    #box_for_spec(students, medium)