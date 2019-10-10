import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append( r"D:\Work\bac_stats\stats_bac")

import pandas as pd
import numpy as np
from classes.student import *
from create_stats.make_histogram import make_histogram

input_csv_file = r'D:\Work\bac_stats\Data\good_bac_2019.csv'

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


if __name__ == "__main__":
    all_students = initialiaze_students(input_csv_file)

    all_students = filter_by_grade(all_students, threshold=5.0)

    boys_students = filter_by_gender( all_students, 'M')
    girls_students = filter_by_gender( all_students, 'F')

    boys_students = filter_by_medium( all_students, 'urban')
    girls_students = filter_by_medium( all_students, 'rural')


    [boys_grades] = return_grades_as_array([boys_students])
    [girls_grades] = return_grades_as_array([girls_students])

    boys_points = create_histogram_array(boys_grades)
    girls_points = create_histogram_array(girls_grades)

    make_histogram([boys_points, girls_points], colors=['blue', 'orange'])
