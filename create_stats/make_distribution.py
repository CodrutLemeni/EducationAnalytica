import sys
import os
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path
from classes.student import initialize_students

input_csv_file_2019 = Path("../data/2019/unitati_scolare_2019.csv")


def add_plot(grades):
    for idx,val in enumerate(grades):
        temp = int(val*100)
        grades [idx] = int(temp/25)*25/100

    d = Counter(grades)
    
    lists = sorted(d.items()) # sorted by key, return a list of tuples

    x, y = zip(*lists) # unpack a list of pairs into two tuples

    plt.plot(x, y)


if __name__ == "__main__":
    all_students_2019 = initialiaze_students(input_csv_file_2019)

    all_students_2019 = filter_by_grade( all_students_2019, 5)
    all_students_2019 = filter_by_medium( all_students_2019, 'rural')

    boys_students = filter_by_gender( all_students_2019, 'M')
    girls_students = filter_by_gender( all_students_2019, 'F')

    [boys_grades] = return_grades_as_array([boys_students])

    add_plot(boys_grades) 

    [girls_grades] = return_grades_as_array([girls_students])
    add_plot(girls_grades)


    plt.show()

