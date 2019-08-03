fin = open( 'data.txt' )
text = fin.read()
fin.close()

text = text.replace('\';LuatDePe_BacalaureatEduRo','')
text = text.replace('<br>','')
text = text.replace('\"','')
text = text.replace('[','')
text = text.replace(']=',' ')
text = text.replace(';','')

students = str(text).split(']')
students = str(students).split(',')


fout = open("nice_data.txt", "w")

for cr_student in students:
    cr_student = cr_student.replace('\'','')
    cr_student = cr_student.replace('\"','')

    fout.write(cr_student)
    fout.write('\n')


fout.close()





print( students )
