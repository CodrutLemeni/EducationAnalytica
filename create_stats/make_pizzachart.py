<<<<<<< HEAD
import sys
sys.path.append( r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics')
import numpy as np
import matplotlib.pyplot as plt
def make_pizzachart(numbers, labels, colors, title, legend = ['A','B']):
=======
import matplotlib.pyplot as plt

def make_pizzachart(numbers, labels, title, legend = ['A','B']):
>>>>>>> master
    plt.pie(numbers, autopct='%1.1f%%', shadow = True, startangle = 140, radius = 1.9)
    plt.legend(labels)
    plt.axis('equal')
    plt.title(title)
    plt.show()