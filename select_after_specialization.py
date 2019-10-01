students_file = open('nice_data.txt','r')
spec_file = open('specialization_list.txt','r')

mate_file = open('mate_info.txt','w')


students = students_file.read()
students = students.split('\n')
specs = spec_file.read()
specs = specs.split('\n')

for (cr_student, cr_spec) in zip( students, specs):
    if cr_spec =='MATEMATICA INFORMATICA':
        mate_file.write( cr_student+'\n')

