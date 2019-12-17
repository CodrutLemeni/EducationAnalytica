import os
import sys
import pandas as pd
import logging

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

from classes.student import initialize_students, return_grades_as_array, get_gender_distribution
from filters.student_filters import filter_all
from create_stats.make_boxplot import make_boxplot
from create_stats.make_pizzachart import make_pizzachart
from create_stats.grade_distribution import plot_grade_distribution

export_path = os.path.join(dirpath, r"plots")

def save_boxplots(students, title, medium):
    current_export_path = os.path.join(export_path,"boxplots")
    current_export_path = os.path.join(current_export_path, medium)

    if( os.path.exists(current_export_path) == False):
        os.mkdir(current_export_path)
    
    current_export_path = os.path.join(current_export_path,title)

    mate_info_boys = filter_all(students, specialisation="matematica-informatica", gender="M")
    filo_boys = filter_all(students, specialisation="filologie", gender="M")
    stiinte_boys = filter_all(students, specialisation="stiinte ale naturii", gender="M")

    mate_info_girls = filter_all(students, specialisation="matematica-informatica", gender="F")
    filo_girls = filter_all(students, specialisation="filologie", gender="F")
    stiinte_girls = filter_all(students, specialisation="stiinte ale naturii", gender="F")

    grades = return_grades_as_array([mate_info_boys, mate_info_girls,
                                    filo_boys, filo_girls,
                                    stiinte_boys, stiinte_girls])

    make_boxplot(grades, current_export_path, ["MATE-INFO", "FILO", "STIINTE"], title=title,medium=medium)    

def save_grade_distribution(input_csv, export_path, year):
    df = pd.read_csv(input_csv)
    
    export_path = os.path.join(export_path, "Grade Distribution")
    if( os.path.exists(export_path) == False):
        os.mkdir(export_path)            
    export_path = os.path.join(export_path,f"{year}")
    plot_grade_distribution(df, 'all', 'hist', export_path)    

def save_circle_plots(students, title, medium):
    current_export_path = os.path.join(export_path,"circle_plots")
    current_export_path = os.path.join(current_export_path, medium)

    if( os.path.exists(current_export_path) == False):
        os.mkdir(current_export_path)
    current_export_path = os.path.join(current_export_path,title)


if __name__ == "__main__":
    base_path = os.path.join(dirpath, r"data")

    for year in range(2015,2020):
        try:
            csv_path = os.path.join(base_path, "good_bac_"+str(year)+".csv" )
            all_students = initialize_students(csv_path)
            all_students = filter_all(all_students, grade=5)
            urban_students = filter_all(all_students, medium="urban")
            rural_students = filter_all(all_students, medium="rural")

# -------------------------------------------BOXPLOTS----------------------------------            
            save_boxplots(all_students, str(year), "general")
            save_boxplots(urban_students, str(year), "urban")
            save_boxplots(rural_students, str(year), "rural")
# -------------------------------------------CIRCLE PLOTS-------------------------------
            # colors = ['blue', 'red']
            # for cr_specialisation in ["matematica-informatica","filologie"]:
            #     cr_students = filter_all(all_students, specialisation=cr_specialisation)
            #     numbers = get_gender_distribution(all_students)
            #     labels = ['Boys', 'Girls']
            #     make_pizzachart(numbers, labels, str(year) + cr_specialisation)
# -------------------------------------------LINE PLOTS-------------------------------

# -------------------------------------------HISTOGRAMS-------------------------------

# -------------------------------------------GRADE DISTRIBUTION-------------------------------
            save_grade_distribution(csv_path,export_path,year)

        except Exception as e:
            # logging.log(e)
            # logging.log(e)
            
            print(f"Year {year} went wrong")

