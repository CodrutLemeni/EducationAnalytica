import numpy as np
import matplotlib.pyplot as plt
import statistics

input_file = r"D:\Work\bac_stats\stats_bac\data\2018\gender_results.txt"
# input_file = r"D:\Work\bac_stats\stats_bac\data\2019\gender_results.txt"
# input_file = r"D:\Work\bac_stats\stats_bac\data\specializations\mate_info.txt"
# input_file = r"D:\Work\bac_stats\stats_bac\data\specializations\filologie.txt"

def read_data(input_file):
    fin = open(input_file)

    grades = fin.read()
    grades = grades.split('\n')

    boys_grades = []
    girls_grades = []
    unknown_grades = []

    for cr_grade in grades:
        cr_grade = cr_grade.split(' ')
        if cr_grade[0] == 'M':
            boys_grades.append( float(cr_grade[-1]) )
        elif cr_grade[0] == 'F':
            girls_grades.append( float(cr_grade[-1]) )
        else:
            unknown_grades.append( float(cr_grade[-1]) )
    return boys_grades, girls_grades, unknown_grades

def create_histogram_array(grades):
    histogram = [0]*5

    # for [idx,cr_grade] in enumerate(grades):
    #     histogram[idx] = int(cr_grade)
    #     if histogram[idx] == 10:
    #         histogram[idx] = 9
    for cr_grade in grades:
        if cr_grade >= 5.00 and cr_grade < 6.00:
            histogram[0] = histogram[0] + 1
        elif cr_grade >= 6.00 and cr_grade < 7.00:
            histogram[1] = histogram[1] + 1
        elif cr_grade >= 7.00 and cr_grade < 8.00:
            histogram[2] = histogram[2] + 1
        elif cr_grade >= 8.00 and cr_grade < 9.00:
            histogram[3] = histogram[3] + 1
        elif cr_grade >= 9.00 and cr_grade <= 10.00:
            histogram[4] = histogram[4] + 1
    
    return histogram

def make_histogram(boys_grades, girls_grades):
    boys_histogram = create_histogram_array(boys_grades)
    girls_histogram = create_histogram_array(girls_grades)

    boys_histogram = np.array(boys_histogram)/len(boys_grades)*100
    girls_histogram = np.array(girls_histogram)/len(girls_grades)*100

    boys_histogram = boys_histogram.astype(int)
    girls_histogram = girls_histogram.astype(int)

    plot_boys=[]
    plot_girls=[]
    for (idx, val) in enumerate(boys_histogram):
        for i in range(val):
            plot_boys.append(idx+5.5)

    for (idx, val) in enumerate(girls_histogram):
        for i in range(val):
            plot_girls.append(idx+5.5)

    plt.hist( [plot_boys,plot_girls], color=['blue', 'orange'], rwidth=2 )
    plt.legend(['Baieti', 'Fete'])
    plt.ylabel('Procentaj')
    plt.xlabel('Note')
    plt.title('Bac_2018')
    plt.xticks(range(5,11))
    plt.yticks(range(0,40,5))
    # plt.hist( [boys_grades,girls_grades], 5)

    plt.show()

if __name__ == "__main__":
    boys_grades, girls_grades, unknown_grades = read_data(input_file)     
    make_histogram( boys_grades, girls_grades)


print('Girls mean: ', statistics.mean(girls_grades))
print('Boys mean: ', statistics.mean(boys_grades))

# plt.plot(girls_grades , label='f')
# plt.plot(boys_grades, label ='b')



# pylab.legend(loc='upper left')
# pylab.show()