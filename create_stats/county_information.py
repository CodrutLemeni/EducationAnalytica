import sys
from os import path
import os.path
from pathlib import Path
import glob
from classes.student import *
from classes.highschool import *
from filters.student_filters import filter_all
from create_stats.make_linegraph import make_linegraph
import pandas as pd
import matplotlib.pyplot as plt
#in what quantile are you with the grade you have, depending on the profile

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
input_csv_students = Path("../data")
input_csv_units = Path("../unitati_scolare_2019.csv")

def get_county_means(filename_students):
    means = []
    counties_used = []
    all_students = initialize_students(filename_students, input_csv_units)
    count_noregion =0
    for current_student in all_students:
        if current_student.highschool.region not in counties_used:
            student_countyx = filter_all(all_students, region=current_student.highschool.region)
            counties_used.append(current_student.highschool.region)
            grades = returngrades(student_countyx)
            means.append(sum(grades) / len(grades))
        if (current_student.highschool.name=="?"):
            count_noregion=count_noregion+1
    #the code of the institution cannot be found
    print(count_noregion)
    counties_used.sort()
    data = {
            'Judet': counties_used,
            'Medie bac': means
           }
    df=pd.DataFrame(data)
    df.sort_values(by=['Judet'])
    return df

if __name__== "__main__":
    year=[2015,2016,2017,2019]
    i = 0
    all_files = glob.glob(os.path.join(input_csv_students, "*.csv"))
    current_export_path = os.path.join(dirpath, 'tables')

    if (os.path.exists(current_export_path) == False):
        os.mkdir(current_export_path)

    current_export_path = os.path.join(current_export_path, 'CountyMeans.xlsx')
    writer = pd.ExcelWriter(current_export_path, engine='xlsxwriter')
    for filename_students in all_files:

        if filename_students.endswith(".csv"):
            print(filename_students)
            county_means = get_county_means(filename_students)
            county_means.to_excel(writer, sheet_name=str(year[i]))
            i=i+1
    writer.save()
    writer.close()

