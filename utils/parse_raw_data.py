input_file=r"D:\Work\bac_stats\stats_bac\all_data\raw_data.txt"
output_file = r"D:\Work\bac_stats\stats_bac\all_data\parsed_data.txt"

fin = open(input_file)
text = fin.read()
fin.close()

text = text.replace('\';LuatDePe_BacalaureatEduRo','')
text = text.replace('<br>','')
text = text.replace('\"','')
text = text.replace('[','')
text = text.replace(']=',' ')
text = text.replace(';','')
text = text.replace('\n','')

students = str(text).split(']')
students = str(students).split(',')

fout = open(output_file, "w")

for cr_student in students:
    cr_student = cr_student.replace('\'','')
    cr_student = cr_student.replace('\"','')

    fout.write(cr_student)
    fout.write('\n')

fout.close()

# print(students)
