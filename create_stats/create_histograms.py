import sys
from pathlib import Path
import os
dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

import numpy as np
from classes.student import *
from create_stats.make_histogram import make_histogram

input_csv_file_2019 = Path("../data/2019/good_bac_2019.csv")

def create_histogram_array(grades):
    histogram = [0]*5

    for cr_grade in grades:
        if cr_grade >= 5.00 and cr_grade < 6.00:
            histogram[0] = histogram[0] + 1
        elif cr_grade >= 6.00 and cr_grade < 7.00:
            histogram[1] = histogram[1] + 1
        elif cr_grade >= 7.00 and cr_grade < 8.00:
            histogram[2] = histogram[2] + 1
        elif cr_grade >= 8.00 and cr_grade < 9.00:
            histogram[3] = histogram[3] + 1
        elif cr_grade >= 9.00 and cr_grade <= 10.00:
            histogram[4] = histogram[4] + 1
        
    histogram = np.array(histogram)/len(grades)*100
    histogram = histogram.astype(int)
    
    plot_points=[]
    for (idx, val) in enumerate(histogram):
        for i in range(val):
            if idx == 0:
                plot_points.append(idx+5)             
            else:
                plot_points.append(idx+5.999)
    return plot_points

def make_gender_histogram(all_students, title):
    all_students = filter_by_grade(all_students, threshold=5.0)

    boys_students = filter_by_gender( all_students, 'M')
    girls_students = filter_by_gender( all_students, 'F')

    [boys_grades, girls_grades] = return_grades_as_array([boys_students, girls_students])

    boys_points = create_histogram_array(boys_grades)
    girls_points = create_histogram_array(girls_grades)

    make_histogram([boys_points, girls_points], colors=['blue', 'orange'], title=title)

def make_medium_histogram(all_students, title):
    all_students = filter_by_grade(all_students, threshold=5.0)

    boys_students = filter_by_medium( all_students, 'urban')
    girls_students = filter_by_medium( all_students, 'rural')

    [boys_grades, girls_grades] = return_grades_as_array([boys_students, girls_students])

    boys_points = create_histogram_array(boys_grades)
    girls_points = create_histogram_array(girls_grades)

    make_histogram([boys_points, girls_points], colors=['blue', 'green'], title=title, legend=["urban","rural"])

if __name__ == "__main__":
    all_students_2019 = initialize_students(input_csv_file_2019)

    make_gender_histogram(all_students_2019, "BAC 2019 gender")
    make_medium_histogram(all_students_2019, "BAC 2019 medium")

