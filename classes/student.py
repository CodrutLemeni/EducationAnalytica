import csv
import sys
sys.path.append(r'../')
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


def initialiaze_students(results_csv_file, schools_csv_file = None):
    '''
        Input:  a csv file containing students
        Output: a list of Students
    '''
    highschools = {}

    if schools_csv_file is not None:
        highschools = create_dictionary(schools_csv_file)
        
    with open(results_csv_file ) as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        not_appear = 0
        unidentified_highschools = []
        students = []
        for row in csv_reader:
            # print(line_count)
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
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
        # print(f'Processed {line_count} lines.')
        # print(' '.join(unidentified_highschools))
        return students

#def filter_by_medium

def filter_by_specialisation(all_students, specialisation):
    '''
        Input:  list of students
                specific specialisation
        Output: list of students with given specialisation
    '''
    selected_students = []
    for current_student in all_students:
        if current_student.specialisation == specialisation:
            selected_students.append(current_student)
    return selected_students

def filter_by_grade(all_students, threshold):
    '''
        Input: list of Students
        Output: list of Students with grades
                    greather than threshold
    '''
    selected_students = []
    for current_student in all_students:
        if current_student.final_grade >= threshold:
            selected_students.append(current_student)
    return selected_students

def filter_by_gender(all_students, gender):
    '''
        Input:  list of students
                specific gender
        Output: list of students with given gender
    '''
    selected_students = []
    for current_student in all_students:
        if current_student.gender == gender:
            selected_students.append(current_student)
    return selected_students    

def filter_by_medium(all_students, medium):
    '''
        Input:  list of students
                specific medium
        Output: list of students with given medium
    '''
    selected_students = []
    for current_student in all_students:
        if current_student.medium == medium:
            selected_students.append(current_student)
    return selected_students    

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


if __name__ == "__main__":
    
    results_csv_file = r'../data/2019/good_bac_2019.csv'
    schools_csv_file = r'../data/2019/unitati_scolare_2019.csv'

    all_students = initialiaze_students(results_csv_file, schools_csv_file)
    mate_info_students = filter_by_specialisation(all_students, 'matematica-informatica' )
