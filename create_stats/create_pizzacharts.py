import sys
import os
<<<<<<< HEAD
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 
=======

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
>>>>>>> made create all_plots function

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from create_stats.make_pizzachart import *
from classes.student import *
from filters.student_filters import filter_all


input_csv_file_2019 = os.path.join(dirpath, r"data")
input_csv_file_2019 = os.path.join(input_csv_file_2019, r"good_bac_2019.csv")

export_path = os.path.join(dirpath,"plots")
export_path = os.path.join(export_path,"test")


def make_gender_pizzachart(all_students, specialisation, title):
    all_students = filter_all(all_students, specialisation=specialisation)
    boys,girls = get_gender_distribution(all_students)
    labels = 'Boys', 'Girls'
    numbers = [boys, girls]
    colors = ['blue', 'red']
    make_pizzachart(numbers, labels, title + specialisation, export_path)


def make_third_option_pizzachart(all_students, specialisation, title):
    subjects_name = load_subjects()
    dimension = len(subjects_name)
    indexes = []
    subjects_distribution = np.zeros(dimension)
    all_students = filter_all(all_students, specialisation=specialisation)

    for student in all_students:
        subjects_distribution[subjects_name.index(student.subject3)] += 1

    for i in range(dimension):
        if subjects_distribution[i] == 0:
            indexes.append(i)
    subjects_distribution = np.delete(subjects_distribution, indexes)
   
    count = 0
    for i in range(len(indexes)):
        subjects_name.pop(indexes[i] - count)
        count += 1
    make_pizzachart(subjects_distribution, subjects_name, title + specialisation, export_path=export_path )
       


def load_subjects():
    subjects = []
    count = 0
    with open('subjects.txt') as subjects_file:
        line = subjects_file.readline()
        line = line[:-1]
        subjects.append(line)
        while line:
            line = subjects_file.readline()
            line = line[:-1]
            subjects.append(line)
    return subjects

if __name__ == "__main__":
    all_students = initialize_students(input_csv_file_2019)
    make_gender_pizzachart(all_students, 'filologie', 'BAC 2019 Gender - ')
    # make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Third option - ')
    