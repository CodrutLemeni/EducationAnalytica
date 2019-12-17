import sys
import os

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from create_stats.make_pizzachart import make_pizzachart
from classes.student import *
from filters.student_filters import filter_all

subjects_file_path = os.path.join(dirpath,r"legacy")
subjects_file_path = os.path.join(subjects_file_path, r"utils")
subjects_file_path = os.path.join(subjects_file_path, r"subjects.txt")
input_csv_file_2019 = os.path.join(dirpath, r"data")
input_csv_file_2019 = os.path.join(input_csv_file_2019, r"good_bac_2019.csv")

export_path = os.path.join(dirpath,r"plots")
export_path = os.path.join(export_path, r"Pizza Charts")

def make_gender_pizzachart(all_students, specialization, title, export_path, medium=None, region=None, locality=None, highschool=None, class_name=None):
    all_students = filter_all(all_students, specialisation=specialization, medium=medium, highschool=highschool, locality=locality, class_name=class_name)
    title = title + specialization
    boys,girls = get_gender_distribution(all_students)
    labels = 'Boys', 'Girls'
    numbers = [boys, girls]
    colors = ['blue', 'red']
    make_pizzachart(numbers, labels, title, export_path=os.path.join(export_path, title))


def make_third_option_pizzachart(all_students, specialization, title, export_path, medium=None, gender=None,
                                 region=None, locality=None, highschool=None, class_name=None):
    subjects_name = load_subjects()
    title = title + specialization
    dimension = len(subjects_name)
    indexes = []
    subjects_distribution = np.zeros(dimension)
    all_students = filter_all(all_students, specialisation=specialization, medium=medium, gender=gender,
                              highschool=highschool, locality=locality, class_name=class_name)

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
    make_pizzachart(subjects_distribution, subjects_name, title, export_path=os.path.join(export_path, title))
       


def load_subjects():
    subjects = []
    count = 0
    with open(subjects_file_path) as subjects_file:
        line = subjects_file.readline()
        line = line[:-1]
        subjects.append(line)
        while line:
            line = subjects_file.readline()
            line = line[:-1]
            subjects.append(line)
    return subjects
def create_pizzacharts(all_students, export_path):
     print("Started creating gender pizzacharts")
     make_gender_pizzachart(all_students, 'filologie', 'BAC 2019 Rural Gender - ', export_path, medium='rural')
     make_gender_pizzachart(all_students, 'filologie', 'BAC 2019 Urban Gender - ', export_path, medium='urban')
     make_gender_pizzachart(all_students, 'filologie', 'BAC 2019 Gender - ', export_path)
     make_gender_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Rural Gender - ', export_path, medium='rural')
     make_gender_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Urban Gender - ', export_path, medium='urban')
     make_gender_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Gender - ', export_path)
     make_gender_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Rural Gender - ', export_path, medium='rural')
     make_gender_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Urban Gender - ', export_path, medium='urban')
     make_gender_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Gender - ', export_path)
     make_gender_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Rural Gender - ', export_path, medium='rural')
     make_gender_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Urban Gender - ', export_path, medium='urban')
     make_gender_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Gender - ', export_path)

     print("Finished creating gender pizzacharts\n")

     print("Started creating filologie third option pizzacharts")
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Urban Boys Third option - ', export_path, medium='urban', gender='M')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Urban Girls Third option - ', export_path, medium='urban', gender='F')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Urban Third option - ', export_path, medium='urban')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Rural Boys Third option - ', export_path, medium='rural', gender='M')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Rural Girls Third option - ', export_path, medium='rural', gender='F')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Rural Third option - ', export_path, medium='rural')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Boys Third option - ', export_path, gender='M')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Girls Third option - ', export_path, gender='F')
     make_third_option_pizzachart(all_students, 'filologie', 'BAC 2019 Third option - ', export_path)
     print("Finished creating filologie third option pizzacharts\n")

     print("Started creating mate-info third option pizzacharts")
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Urban Boys Third option - ', export_path, medium='urban', gender='M')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Urban Girls Third option - ', export_path, medium='urban', gender='F')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Urban Third option - ', export_path, medium='urban')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Rural Boys Third option - ', export_path, medium='rural', gender='M')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Rural Girls Third option - ', export_path, medium='rural', gender='F')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Rural Third option - ', export_path, medium='rural')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Boys Third option - ', export_path, gender='M')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Girls Third option - ', export_path, gender='F')
     make_third_option_pizzachart(all_students, 'matematica-informatica', 'BAC 2019 Third option - ', export_path)
     print("Finished creating mate-info third option pizzachart\n")

     print("Started creating stiinte ale naturii third option pizzacharts")
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Urban Boys Third option - ', export_path, medium='urban', gender='M')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Urban Girls Third option - ', export_path, medium='urban', gender='F')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Urban Third option - ', export_path, medium='urban')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Rural Boys Third option - ', export_path, medium='rural', gender='M')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Rural Girls Third option - ', export_path, medium='rural', gender='F')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Rural Third option - ', export_path, medium='rural')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Boys Third option - ', export_path, gender='M')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Girls Third option - ', export_path, gender='F')
     make_third_option_pizzachart(all_students, 'stiinte ale naturii', 'BAC 2019 Third option - ', export_path)
     print("Finished creating stiinte ale naturii third option pizzacharts\n")
    
     print("Started creating stiinte sociale third option pizzacharts")
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Urban Boys Third option - ', export_path, medium='urban', gender='M')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Urban Girls Third option - ', export_path, medium='urban', gender='F')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Urban Third option - ', export_path, medium='urban')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Rural Boys Third option - ', export_path, medium='rural', gender='M')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Rural Girls Third option - ', export_path, medium='rural', gender='F')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Rural Third option - ', export_path, medium='rural')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Boys Third option - ', export_path, gender='M')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Girls Third option - ', export_path, gender='F')
     make_third_option_pizzachart(all_students, 'stiinte sociale', 'BAC 2019 Third option - ', export_path)
     print("Finished creating stiinte sociale third option pizzacharts\n")

if __name__ == "__main__":
    all_students = initialize_students(input_csv_file_2019)
    create_pizzacharts(all_students, export_path)
    