import sys
import os
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import csv
from classes.school import remove_left_zeros
from classes.schoolsList import SchoolList
from filters.student_filters import *
class Scholar:
    def __init__(self, gender, medium, school,
                   subject1, subject2, subject1_grade_init, subject2_grade_init, appeal_1,
                   appeal_2,  subject1_grade_final, subject2_grade_final,
                   final_grade, middle_school_grade):
        self.gender               = gender
        self.medium               = medium.lower()
        self.appeal_1             = appeal_1
        self.appeal_2             = appeal_2
        self.school               = school
        self.subject1             = subject1.lower()
        self.subject2             = subject2.lower()
        self.subject1_grade_init  = float(subject1_grade_init)
        self.subject2_grade_init  = float(subject2_grade_init)
        self.subject1_grade_final = float(subject1_grade_final)
        self.subject2_grade_final = float(subject2_grade_final)
        self.medium_school_grade  = float(middle_school_grade)
        self.final_grade          = float(final_grade)

        if self.appeal_1 == "DA":
            self.appeal_1 = 1
        else:
            self.appeal_1 = 0

        if self.appeal_1 == "DA":
            self.appeal_1 = 1
        else:
            self.appeal_1 = 0



    def __str__(self):
        return "damar"


def initialize_scholars(results_csv_file, base_path):
    '''
        Input:  a csv file containing students
        Output: a list of Students
    '''
    schools = SchoolList(base_path)
    with open(results_csv_file, encoding='utf8' ) as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        students = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                if row[4] == "ABSENT" or row[6] == "ABSENT" or row[19] == "":
                    continue
                row[3] = remove_left_zeros(row[3])
                school = schools.get_school(row[3])
                current_student = Scholar(row[1], row[2], school, "matematica", "romana",
                                    row[7], row[9], row[10], row[14], row[16], row[18],
                                    row[19], row[20])
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
    '''
        Input: list of Students
        Output: number of male and
                number of female students
    '''
    boys  = 0
    girls = 0
    for student in all_students:
        if student.gender == 'M':
            boys  = boys + 1
        else:
            girls = girls + 1
    return boys, girls

def return_subject_grades(all_scholars):
    '''
        Output: 2 lists containing grades for each subject
    '''
    list_1, list_2 = [], []
    for student in all_scholars:
        list_1.append(student.subject1_grade_final)
        list_2.append(student.subject2_grade_final)

    return list_1, list_2

if __name__ == "__main__":
    base_path = os.path.join(dirpath, r"data")
    csv_file = os.path.join(base_path, 'good_evn_2019.csv')
    all_students = initialize_scholars(csv_file, base_path)
    students = filter_by_grade(all_students, 6.0)