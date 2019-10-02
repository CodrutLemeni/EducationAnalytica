input_file=r'D:\Work\bac_stats\stats_bac\data\gender_results.txt'
specialization_file = r'D:\Work\bac_stats\stats_bac\data\specialization_list.txt'


students_file = open(input_file,'r')
spec_file = open(specialization_file,'r')

mate_file = open(r'D:\Work\bac_stats\stats_bac\data\mate_info.txt','w')
stiinte_naturii_file = open(r'D:\Work\bac_stats\stats_bac\data\stiinte_naturii.txt','w')
filologie_file = open(r'D:\Work\bac_stats\stats_bac\data\filologie.txt','w')

students = students_file.read()
students = students.split('\n')
specs = spec_file.read()
specs = specs.split('\n')

for (cr_student, cr_spec) in zip( students, specs):
    if cr_spec =='MATEMATICA INFORMATICA':
        mate_file.write( cr_student+'\n')
    if cr_spec =='STIINTE ALE NATURII':
        stiinte_naturii_file.write( cr_student+'\n')
    if cr_spec =='FILOLOGIE':
        filologie_file.write( cr_student+'\n')