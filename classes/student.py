import sys
import os
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

import csv
from classes.highschool import *
class Student:
    def __init__(self, gender, specialisation, medium, highschool, class_name, passed,
                   subject1, subject1_grade_init, subject1_grade_final, subject2, subject2_grade_init, subject2_grade_final,
                    subject3, subject3_grade_init, subject3_grade_final ):
        self.gender               = gender
        self.specialisation       = specialisation.lower()
        self.medium               = medium.lower()
        self.class_name           = class_name
        self.passed               = passed
        self.highschool           = highschool

        if subject1_grade_final == '':
            subject1_grade_final = subject1_grade_init

        if subject2_grade_final == '':
            subject2_grade_final = subject2_grade_init

        if subject3_grade_final == '':
            subject3_grade_final = subject3_grade_init


        self.subject1             = subject1.lower()
        self.subject1_grade_init  = float(subject1_grade_init)
        self.subject1_grade_final = float(subject1_grade_final)
        self.subject2             = subject2.lower()
        self.subject2_grade_init  = float(subject2_grade_init)
        self.subject2_grade_final = float(subject2_grade_final)
        self.subject3             = subject3.lower()
        self.subject3_grade_init  = float(subject3_grade_init)
        self.subject3_grade_final = float(subject3_grade_final)
        
        self.final_grade          = round ( (self.subject1_grade_final + self.subject2_grade_final + self.subject3_grade_final) / 3, 2)


        def __str__(self):
            return "damar"


def initialize_students(results_csv_file, schools_csv_file = None):
    '''
        Input:  a csv file containing students
        Output: a list of Students
    '''
    highschools = {}

    if schools_csv_file is not None:
        highschools = create_dictionary(schools_csv_file)
        
    with open(results_csv_file, encoding='utf8' ) as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        students = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                row[7] = remove_left_zeros(row[7])
                if not row[7] in highschools:
                    highschool = Highschool( row[7], row[8])
                else:
                    highschool = highschools[row[7]]
                current_student = Student( row[1], row[2], row[6], highschool, row[9], row[50], 
                                    row[10], row[37], row[42],
                                    row[13], row[39], row[46],
                                    row[14], row[40], row[48])
                students.append(current_student)
                line_count += 1
        return students

def return_grades_as_array(specs):
    '''
        Input:  list of lists of students
        Output: list of lists of grades 
    '''
    grades = [ [] for i in range(len(specs)) ]

    for idx in range(len(specs)):
        for x in specs[idx]:
            grades[idx].append(x.final_grade)

    return grades

def get_gender_distribution(all_students):
    boys  = 0
    girls = 0
    for student in all_students:
        if student.gender == 'M':
            boys  = boys + 1
        else:
            girls = girls + 1
    return boys, girls