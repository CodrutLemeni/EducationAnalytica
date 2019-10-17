import sys
<<<<<<< HEAD
sys.path.append( r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics')
import numpy as np
import pandas as pd
=======
sys.path.append(r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics')
import numpy as np
>>>>>>> master
import matplotlib.pyplot as plt
from create_stats.make_pizzachart import *
from classes.student import *

<<<<<<< HEAD
input_csv_file_2019 = r'/home/sebastian/Dropbox/Facultate/BacStats/good_bac_2019.csv'
=======
input_csv_file_2019 = r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics/data/2019/good_bac_2019.csv'
>>>>>>> master

def make_gender_pizzachart(all_students, specialisation,title):
    all_students = filter_by_specialisation(all_students, specialisation)
    boys,girls = get_gender_distribution(all_students)
    labels = 'Boys', 'Girls'
    numbers = [boys, girls]
    colors = ['blue', 'red']
<<<<<<< HEAD
    make_pizzachart(numbers, labels, colors, title + specialisation)
=======
    make_pizzachart(numbers, labels, title + specialisation)
>>>>>>> master


def make_third_option_pizzachart(all_students, specialisation, title):
    subjects_name = load_subjects()
    dimension = len(subjects_name)
    indexes = []
<<<<<<< HEAD
    colors = ['blue', 'green', 'red', 'yellow', 'purple', 'cyan','magenta']
=======
>>>>>>> master
    subjects_distribution = np.zeros(dimension)
    all_students = filter_by_specialisation(all_students,specialisation)

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
<<<<<<< HEAD
    for subject in subjects_distribution:
        print(subject)
    colors = colors[1:len(subjects_name)]
    make_pizzachart(subjects_distribution, subjects_name, colors, title + specialisation )
=======
    make_pizzachart(subjects_distribution, subjects_name, title + specialisation )
>>>>>>> master
       


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
    all_students = initialiaze_students(input_csv_file_2019)
<<<<<<< HEAD
    # make_gender_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Gender - ')
    make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Third option - ')
=======
    make_gender_pizzachart(all_students, 'filologie', 'BAC 2019 Gender - ')
    # make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Third option - ')
>>>>>>> master
