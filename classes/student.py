import csv

class Student:
    def __init__(self, highschool, romanian_grade, county, specialisation, profile_exam_name, profile_exam_grade, optional_exam_name, optional_exam_grade, passed):
        self.highschool          = highschool
        self.romanian_grade      = float(romanian_grade)
        self.county              = county
        self.specialisation      = specialisation
        self.profile_exam_name   = profile_exam_name
        self.profile_exam_grade  = float(profile_exam_grade)
        self.optional_exam_name  = optional_exam_name
        self.optional_exam_grade = float(optional_exam_grade)
        self.passed              = passed
    def __str__(self):
        return str(self.highschool) 

    
def initialiaze_students(csv_file):
    '''
        Input:  a csv file containing students
        Output: a list of Students
    '''

    with open(csv_file) as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        students = []
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                current_student = Student( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
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

if __name__ == "__main__":
    csv_file = r'D:\Work\bac_stats\stats_bac\results.csv'
    all_students = initialiaze_students(csv_file)
    
    mate_info_students = filter_by_specialisation(all_students, 'Â MATEMATICA-INFORMATICA' )
    pass

