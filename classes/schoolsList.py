import csv
import sys
import os

sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
from classes.school import School
class SchoolList:
    def __init__(self, base_path):
        self.csv_file = os.path.join(base_path, "unitati_scolare_2019.csv")
        self.schools_list = create_dictionary(self.csv_file)

    def is_in_school_list(self, SIIR_code):
        if SIIR_code not in self.schools_list:
            return False
        return True
    def get_school(self, SIIR_code):
        '''
            Input: SIIR_CODE
            Output: School object that has SIIR_CODE
        '''
        return self.schools_list[SIIR_code]


def create_dictionary(csv_file):
    '''
    Input:  csv_file containing schools
    Output: dictionary between SIIR_CODE and actual highschool
    '''
    with open(csv_file, encoding='utf8') as file:
        reader = csv.reader(file)
        line_index = 0
        schools = {}
        for row in reader:
            current_highschool = School(row[0], row[1], row[3], row[5], row[16])
            schools[row[0]] = current_highschool
            line_index += 1
    return schools