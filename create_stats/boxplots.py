import matplotlib.pyplot as plt
import sys
import os

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 
from classes.student import initialize_students, return_grades_as_array
from classes.highschool import *
from  create_stats.make_boxplot import *
from filters.student_filters import *


def box_for_spec(all_students, medium=None):
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
    csv_path = os.path.join(dirpath, r"data")
    csv_path = os.path.join(csv_path, r"good_bac_2019.csv")
    # all_students = initialiaze_students(csv_file, schools_csv_file)
    all_students = initialize_students(csv_path)
    
    all_students = filter_by_grade(all_students, 5.0)

    box_for_spec(all_students)
    medium = "urban"
    #medium = "rural"
    students = filter_by_medium( all_students, medium) # second parameter can be "rural" or "urban"
    #box_for_spec(students, medium)