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
from create_stats.create_linegraphs import *
from create_stats.create_barchart import create_barchart_percentage

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

def save_linegraphs(students, years, export_path):
    current_export_path = os.path.join(export_path,"Line Graphs")
    current_export_path = os.path.join(current_export_path)

    if( os.path.exists(current_export_path) == False):
        os.mkdir(current_export_path)
    current_export_path = os.path.join(current_export_path)
    create_all_linegraphs(students, years, current_export_path)

def save_horizontal_bar_chart(all_students, year):
    current_export_path = os.path.join(export_path, "Horizontal Bar Charts")
    if( os.path.exists(current_export_path) == False):
        os.mkdir(current_export_path)
    
    create_barchart_percentage(all_students = all_students, current_export_path = current_export_path, year = year)
    

if __name__ == "__main__":
    base_path = os.path.join(dirpath, r"data")
    students_years = {} # dict containing list of results for each year
    years = [] # available keys for the previous dict
    for year in range(2015,2020):
        try:
            csv_path = os.path.join(base_path, "good_bac_"+str(year)+".csv" )
            all_students = initialize_students(csv_path)
            years.append(str(year)) # results for this year are stored in the dictionary
            students_years[str(year)] = all_students 
            all_students = filter_all(all_students, grade=5)
            urban_students = filter_all(all_students, medium="urban")
            rural_students = filter_all(all_students, medium="rural")

# -------------------------------------------BOXPLOTS----------------------------------       

            logging.info("Started Boxplots from {}".format(year))     
            save_boxplots(all_students, str(year), "general")
            save_boxplots(urban_students, str(year), "urban")
            save_boxplots(rural_students, str(year), "rural")
            logging.info("Finished Boxplots from {}".format(year))     

# -------------------------------------------CIRCLE PLOTS-------------------------------
            logging.info("Started Circle Plots from {}".format(year))     
            colors = ['blue', 'red']
            for cr_specialisation in ["matematica-informatica","filologie"]:
                cr_students = filter_all(all_students, specialisation=cr_specialisation)
                numbers = get_gender_distribution(all_students)
                labels = ['Boys', 'Girls']
                make_pizzachart(numbers, labels, str(year) + cr_specialisation, os.path.join(export_path,"Circle Plots"))
            logging.info("Finished Circle Plots from {}".format(year))     

#--------------------------------------------BAR CHARTS-------------------------------
            logging.info("Started Bar Charts from {}".format(year))
            all_students = initialize_students(csv_path)
            save_horizontal_bar_chart(all_students = all_students, year = year)
            logging.info("Finished Bar Charts from {}".format(year))

# -------------------------------------------LINE PLOTS-------------------------------

# -------------------------------------------HISTOGRAMS-------------------------------

# -------------------------------------------GRADE DISTRIBUTION-------------------------------
            logging.info("Started Grade Distribution from {}".format(year))     
            save_grade_distribution(csv_path,export_path,year)
            logging.info("Finished Grade Distribution from {}".format(year))     


        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            print(f"Year {year} went wrong")
    
    save_linegraphs(students_years, years, export_path)

