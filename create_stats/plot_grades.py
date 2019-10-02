import numpy as np
import matplotlib.pyplot as plt
import pylab 
import statistics

input_file = r"D:\Work\bac_stats\stats_bac\data\gender_results.txt"
input_file = r"D:\Work\bac_stats\stats_bac\data\specializations\mate_info.txt"
input_file = r"D:\Work\bac_stats\stats_bac\data\specializations\filologie.txt"



fin = open(input_file)

grades = fin.read()
grades = grades.split('\n')

boys_grades = []
girls_grades = []
unknown_grades = []

for crGrade in grades:
    crGrade = crGrade.split(' ')
    if crGrade[0] == 'M':
        boys_grades.append( float(crGrade[-1]) )
    elif crGrade[0] == 'F':
        girls_grades.append( float(crGrade[-1]) )
    else:
        unknown_grades.append( float(crGrade[-1]) )


print('Girls mean: ', statistics.mean(girls_grades))
print('Boys mean: ', statistics.mean(boys_grades))

# plt.plot(girls_grades , label='f')
# plt.plot(boys_grades, label ='b')
    


# pylab.legend(loc='upper left')
# pylab.show()