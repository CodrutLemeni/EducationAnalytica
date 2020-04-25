import csv
from pathlib import Path
class Highschool:
    def __init__(self, SIIR_code, SIRUES_code, name = '?', locality = '?', region = '?',property = '?'):
        
        self.SIIR_code       = SIIR_code
        self.SIRUES_code     = SIRUES_code
        self.name            = name.lower()
        self.locality        = locality.lower()
        self.region          = region
	self.property        = property

    def __str__(self):
        return str(self.SIIR_code + ' ' + self.SIRUES_code + ' ' + self.name + ' ' + self.locality
                     + ' ' + self.region)


def create_dictionary(csv_file):
    with open(csv_file, encoding='utf8') as file:
        reader = csv.reader(file)
        line_index = 0
        highschools = {}
        for row in reader:
            current_highschool = Highschool(row[0], row[1], row[3], row[5], row[16],row[14])
            highschools[row[0]] = current_highschool
            line_index += 1
            
    return highschools

# remove zero padding from SIIR_code
def remove_left_zeros(code):
    i = 0
    while code[i] == '0':
	    i += 1
    return code[i:]
    
if __name__ == "__main__":
    csv_file = Path(r'../data/2019/unitati_scolare_2019.csv')
    highschools = create_dictionary(csv_file)
