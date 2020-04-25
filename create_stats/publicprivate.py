import glob
from classes.student import *
from classes.highschool import *
from filters.student_filters import filter_all
from create_stats.make_linegraph import make_linegraph
import pandas as pd
import matplotlib.pyplot as plt

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
input_csv_students = Path("../data")
input_csv_units = Path("../unitati_scolare_2019.csv")

if __name__== "__main__":
    year=[2015,2016,2017,2019]
    all_files = glob.glob(os.path.join(input_csv_students, "*.csv"))
    current_export_path = os.path.join(dirpath, 'plots')
    # make line graph with average of the public vs private institutions
    all_private = []
    all_public = []
    current_export_path = os.path.join(current_export_path, 'publicPrivate')
    i = 0
    for filename_students in all_files:

        if filename_students.endswith(".csv"):
            all_students = initialize_students(filename_students, input_csv_units)
            print(filename_students)
            private_students = filter_all(all_students, property="Privata")
            public_students = filter_all(all_students, property='Publica de interes national Si local')
            i = i + 1
            all_private.append(sum(returngrades(private_students)) / len(returngrades(private_students)))
            all_public.append( sum(returngrades(public_students)) / len(returngrades(public_students)))

    firstplot = plt.plot(year, all_private, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4,label='Institutii private')
    secondplot ,= plt.plot(year, all_public, marker='' , color='olive', linewidth=2,label='Institutii publice')
    axes = plt.gca()
    axes.set_ylim([5, 10])
    axes.legend()
    plt.yticks([5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])
    plt.xticks([2015,2016,2017,2018,2019])
    plt.xlabel('Ani')
    plt.ylabel('Medie bacalaureat')

    plt.savefig(current_export_path)
    plt.show()