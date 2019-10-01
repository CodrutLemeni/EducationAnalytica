import numpy as np
import matplotlib.pyplot as plt
import pylab 


def read_data( input ):
    data = np.genfromtxt(input, delimiter=' ')

    all_students = np.sum(data[:,1])

    data[:,1] = np.cumsum(data[:,1])

    data[:,1] = data[:,1]*100/all_students

    pylab.plot(data[:,0],data[:,1], label = input)

    pass



read_data('final_grades_boys.txt')
read_data('final_grades_girls.txt')
pylab.legend(loc='upper left')
pylab.show()