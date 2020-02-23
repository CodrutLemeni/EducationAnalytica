import os
import sys
import pandas as pd
import logging

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

from classes.student import initialize_students, return_grades_as_array, get_gender_distribution
from filters.student_filters import filter_all
from create_stats.make_barchart import make_barchart_percentage

def create_barchart_percentage(all_students, current_export_path, year):
    current_export_path_1 = os.path.join(current_export_path, "Fete-Baieti")
    if( os.path.exists(current_export_path_1) == False):
        os.mkdir(current_export_path_1)

    current_export_path_1 = os.path.join(current_export_path_1, str(year))

    all_students = filter_all(all_students, grade=5)
    all_boys = filter_all(all_students, gender="M")
    all_girls = filter_all(all_students, gender="F")

    students_list = [all_boys, all_girls]
    name_list = ["Baieti", "Fete"]
    colors = ['#BEEBE9', '#F4DADA']

    make_barchart_percentage(all_categories = students_list, categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti " + str(year)), current_export_path = current_export_path_1, colors = colors)
    current_export_path_2 = os.path.join(current_export_path, "Fete-Baieti mate-info si filo")
    if( os.path.exists(current_export_path_2) == False):
        os.mkdir(current_export_path_2)

    current_export_path2 = os.path.join(current_export_path_2, str(year))

    boys_filo = filter_all(all_students, gender="M", specialisation="filologie")
    girls_filo = filter_all(all_students, gender="F", specialisation="filologie")
    boys_mate_info = filter_all(all_students, gender="M", specialisation="matematica-informatica")
    girls_mate_info = filter_all(all_students, gender="F", specialisation="matematica-informatica")
    colors = ['#BEEBE9', '#F4DADA', '#BEEBE9', '#F4DADA']

    students_list = [boys_filo, girls_filo, boys_mate_info, girls_mate_info]
    name_list = ["Baieti \nfilologie",  "Fete  \nfilologie", "Baieti   \nmate-info", "Fete    \nmate-info"]
    make_barchart_percentage(all_categories = students_list, categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti mate-info si filologie " + str(year)), current_export_path = current_export_path2, colors = colors)