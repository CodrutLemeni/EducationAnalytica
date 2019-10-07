import csv

class Student:
    def __init__(self, gender, specialisation, medium, highschool_SIIIR, highschool_SIRUES, class_name, passed,
                   subject1, subject1_grade_init, subject1_grade_final, subject2, subject2_grade_init, subject2_grade_final,
                    subject3, subject3_grade_init, subject3_grade_final ):
        self.gender               = gender
        self.specialisation       = specialisation.lower()
        self.medium               = medium
        self.highschool_SIIIR     = highschool_SIIIR
        self.highschool_SIRUES    = highschool_SIRUES
        self.class_name           = class_name
        self.passed               = passed

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


    # def __str__(self):
    #     return str(self.highschool)


def initialiaze_students(csv_file):
    '''
        Input:  a csv file containing students
        Output: a list of Students
    '''

    with open(csv_file, encoding="utf8") as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        students = []
        for row in csv_reader:
            # print(line_count)
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                current_student = Student( row[1], row[2], row[6], row[7], row[8], row[9], row[50], 
                                    row[10], row[37], row[42],
                                    row[13], row[39], row[46],
                                    row[14], row[40], row[48])
                # print( current_student )
                students.append(current_student)
                line_count += 1
        # print(f'Processed {line_count} lines.')
        return students

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
                    greather than 5.0
    '''
    selected_students = []
    for current_student in all_students:
        if current_student.final_grade >= threshold:
            selected_students.append(current_student)
    return selected_students


if __name__ == "__main__":
    csv_file = r'D:\Work\bac_stats\Data\good_bac_2019.csv'
    all_students = initialiaze_students(csv_file)

    mate_info_students = filter_by_specialisation(all_students, 'matematica-informatica' )
    pass
