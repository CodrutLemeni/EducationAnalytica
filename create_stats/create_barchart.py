import os
import sys
import pandas as pd
import logging

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

from classes.student import initialize_students, return_grades_as_array, get_gender_distribution
from filters.student_filters import filter_all
from create_stats.make_barchart import make_barchart_percentage
from create_stats.make_barchart import make_barchart_values

def create_barchart_percentage(all_students, current_export_path, year):
    current_export_path_1 = os.path.join(current_export_path, "Fete-Baieti")
    if( os.path.exists(current_export_path_1) == False):
        os.mkdir(current_export_path_1)

    current_export_path_1 = os.path.join(current_export_path_1, str(year))

    all_students_passed = filter_all(all_students, passed="Promovat")
    all_boys = filter_all(all_students, gender="M")
    all_girls = filter_all(all_students, gender="F")

    all_boys_passed = filter_all(all_students_passed, gender="M")
    all_girls_passed = filter_all(all_students_passed, gender="F")
    

    students_list = [all_boys, all_girls]
    students_list_passed = [all_boys_passed, all_girls_passed]
    name_list = ["Baieti", "Fete"]
    colors = ['#BEEBE9', '#F4DADA']

    make_barchart_percentage(all_categories = students_list, all_categories_good = students_list_passed, categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti " + str(year)), current_export_path = current_export_path_1, colors = colors)
    
    
    
    current_export_path_2 = os.path.join(current_export_path, "Fete-Baieti mate-info, filo si stiinte")
    if( os.path.exists(current_export_path_2) == False):
        os.mkdir(current_export_path_2)

    current_export_path2 = os.path.join(current_export_path_2, str(year))

    boys_filo = filter_all(all_students, gender="M", specialisation="filologie")
    girls_filo = filter_all(all_students, gender="F", specialisation="filologie")
    boys_mate_info = filter_all(all_students, gender="M", specialisation="matematica-informatica")
    girls_mate_info = filter_all(all_students, gender="F", specialisation="matematica-informatica")
    boys_stiinte = filter_all(all_students, gender="M", specialisation="stiinte ale naturii")
    girls_stiinte = filter_all(all_students, gender="F", specialisation="stiinte ale naturii")
    colors = ['#BEEBE9', '#F4DADA', '#BEEBE9', '#F4DADA', '#BEEBE9', '#F4DADA']

    students_list = [boys_filo, girls_filo, boys_mate_info, girls_mate_info, boys_stiinte, girls_stiinte]
    name_list = ["Baieti \nfilologie",  "Fete  \nfilologie", "Baieti   \nmate-info", "Fete    \nmate-info", "Baieti \nstiinte", "Fete  \nstiinte"]
    
    students_list_passed = []

    for crt_student_list in students_list:
        students_list_passed.append(filter_all(crt_student_list,passed = "Promovat"))
    
    make_barchart_percentage(all_categories = students_list, all_categories_good = students_list_passed,categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti \nmate-info, filologie si stiinte ale naturii" + str(year)), current_export_path = current_export_path2, colors = colors)




    mate_info = filter_all(all_students, specialisation="matematica-informatica")
    stiinte = filter_all(all_students, specialisation="stiinte ale naturii")

    grade_mate_info_romana = 0
    grade_stiinte_romana = 0

    for element in mate_info:
        grade_mate_info_romana += element.subject1_grade_final

    for element in stiinte:
        grade_stiinte_romana += element.subject1_grade_final

    current_export_path_3 = os.path.join(current_export_path, "Romana mate-info si stiinte")
    if( os.path.exists(current_export_path_3) == False):
        os.mkdir(current_export_path_3)

    current_export_path_3 = os.path.join(current_export_path_3, str(year))

    grade_mate_info_romana = float(grade_mate_info_romana) / float(len(mate_info))
    grade_stiinte_romana = float(grade_stiinte_romana) / float(len(stiinte))
    grades = [grade_mate_info_romana, grade_stiinte_romana]
    make_barchart_values(grades, ["mate-info", "stiinte"], "Note romana", current_export_path_3, ['#BEEBE9', '#F4DADA'])
