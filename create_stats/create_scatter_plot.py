import os
import sys

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

from filters.student_filters import filter_all
from classes.student import returngrades
from make_scatter_plot import make_scatter_plot

def create_scatter_plot(all_students, current_export_path, current_export_path_js, year, percentage):

    #------procent promovabilitate general fete-baieti--------
    current_export_path_1 = os.path.join(current_export_path, "Medii vs Prezenta Vot")
    if( os.path.exists(current_export_path_1) == False):
        os.mkdir(current_export_path_1)
    current_export_path_1 = os.path.join(current_export_path_1, str(year))
    
    current_export_path_1_js = os.path.join(current_export_path_js, "Medii vs Prezenta Vot")
    if( os.path.exists(current_export_path_1_js) == False):
        os.mkdir(current_export_path_1_js)
    current_export_path_1_js = os.path.join(current_export_path_1_js, str(year))

    means = []
    counties_used = []
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
    
    average_counties = {}
    for i in range(len(counties_used)):
        crt_county = counties_used[i]
        if crt_county == '?':
            continue
        average_counties[crt_county] = means[i]
    
    make_scatter_plot(ox_values = average_counties, oy_values = percentage, ox_name = "Medie Judete", oy_name = "Prezenta la vot", title = "Medii vs Prezenta Vot", current_export_path = current_export_path_1)
    

    

    

    