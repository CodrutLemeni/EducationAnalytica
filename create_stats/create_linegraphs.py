import sys
import os
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
import statistics
from filters.student_filters import filter_all
from create_stats.make_linegraph import make_linegraph
from read_data.read_students import read_results

def create_all_linegraphs(all_students, years, export_path):
 print("Started creating gender line graphs")
 create_gender_linegraph(all_students, years, "Boys vs Girls GPA", export_path)
 create_gender_linegraph(all_students, years, "Urban Boys vs Urban Girls GPA", export_path, "urban")
 create_gender_linegraph(all_students, years, "Rural Boys vs Rural Girls GPA", export_path, "rural")
 print("Finished creating gender line graphs\n")

 print("Started creating medium line graphs")
 create_medium_linegraph(all_students, years, "Urban vs Rural", export_path)
 create_medium_linegraph(all_students, years, "Urban Boys vs Rural Boys", export_path, 'M')
 create_medium_linegraph(all_students, years, "Urban Girls vs Rural Girls", export_path, 'F')
 print("Finished creating medium line graphs\n")


 print("Started creating mate-info line graphs")
 create_specialization_linegraph(all_students, years, "mate-info vs stiinte ale naturii GPA", export_path, "matematica-informatica", "stiinte ale naturii")
 create_specialization_linegraph(all_students, years, "mate-info rural vs stiinte ale naturii rural GPA", export_path, "matematica-informatica",
                                                      "stiinte ale naturii", medium='rural')
 create_specialization_linegraph(all_students, years, "mate-info rural boys vs stiinte ale naturii rural boys GPA", export_path, "matematica-informatica",
                                                      "stiinte ale naturii", medium='rural', gender="M")
 create_specialization_linegraph(all_students, years, "mate-info rural girls vs rural stiinte ale naturii rural girls GPA", export_path,
                                                      "matematica-informatica","stiinte ale naturii", medium='rural', gender="F")
 create_specialization_linegraph(all_students, years, "mate-info urban vs stiinte ale naturii urban GPA", export_path, "matematica-informatica",
                                                      "stiinte ale naturii", medium='urban')
 create_specialization_linegraph(all_students, years, "mate-info urban boys vs stiinte ale naturii urban boys GPA", export_path, "matematica-informatica",
                                                      "stiinte ale naturii", medium='urban', gender="M")
 create_specialization_linegraph(all_students, years, "mate-info urban girls vs stiinte ale naturii urban girls GPA", export_path, "matematica-informatica",
                                                      "stiinte ale naturii", medium='urban', gender="F")
 create_specialization_linegraph(all_students, years, "mate-info vs filologie GPA", export_path, "matematica-informatica", "filologie")
 create_specialization_linegraph(all_students, years, "mate-info rural vs filologie rural GPA", export_path, "matematica-informatica",
                                                      "filologie", medium='rural')
 create_specialization_linegraph(all_students, years, "mate-info rural boys vs filologie rural boys GPA", export_path, "matematica-informatica",
                                                      "filologie", medium='rural', gender="M")
 create_specialization_linegraph(all_students, years, "mate-info rural girls vs rural filologie rural girls GPA", export_path, "matematica-informatica",
                                                      "filologie", medium='rural', gender="F")
 create_specialization_linegraph(all_students, years, "mate-info urban vs filologie urban GPA", export_path, "matematica-informatica",
                                                      "filologie", medium='urban')
 create_specialization_linegraph(all_students, years, "mate-info urban boys vs filologie urban boys GPA", export_path, "matematica-informatica",
                                                      "filologie", medium='urban', gender="M")
 create_specialization_linegraph(all_students, years, "mate-info urban girls vs filologie urban girls GPA", export_path, "matematica-informatica",
                                                      "filologie", medium='urban', gender="F")
 create_specialization_linegraph(all_students, years, "mate-info vs stiinte sociale GPA", export_path, "matematica-informatica", "stiinte sociale")
 create_specialization_linegraph(all_students, years, "mate-info rural vs stiinte sociale rural GPA", export_path, "matematica-informatica",
                                                      "stiinte sociale", medium='rural')
 create_specialization_linegraph(all_students, years, "mate-info rural boys vs stiinte sociale rural boys GPA", export_path, "matematica-informatica",
                                                      "stiinte sociale", medium='rural', gender="M")
 create_specialization_linegraph(all_students, years, "mate-info rural girls vs rural stiinte sociale rural girls GPA", export_path, "matematica-informatica",
                                                      "stiinte sociale", medium='rural', gender="F")
 create_specialization_linegraph(all_students, years, "mate-info urban vs stiinte sociale urban GPA", export_path, "matematica-informatica",
                                                      "stiinte sociale", medium='urban')
 create_specialization_linegraph(all_students, years, "mate-info urban boys vs stiinte sociale urban boys GPA", export_path, "matematica-informatica",
                                                      "stiinte sociale", medium='urban', gender="M")
 create_specialization_linegraph(all_students, years, "mate-info urban girls vs stiinte sociale urban girls GPA", export_path, "matematica-informatica",
                                                      "stiinte sociale", medium='urban', gender="F")
 print("Finished creating mate-info line graphs\n")

 print("Started creating stiinte ale naturii line graphs")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii vs filologie GPA", export_path, "stiinte ale naturii", "filologie")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii rural vs filologie rural GPA", export_path, "stiinte ale naturii",
                                                      "filologie", medium='rural')
 create_specialization_linegraph(all_students, years, "stiinte ale naturii rural boys vs filologie rural boys GPA", export_path, "stiinte ale naturii",
                                                      "filologie", medium='rural', gender="M")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii rural girls vs rural filologie rural girls GPA", export_path, "stiinte ale naturii",
                                                      "filologie", medium='rural', gender="F")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii urban vs filologie urban GPA", export_path, "stiinte ale naturii",
                                                      "filologie", medium='urban')
 create_specialization_linegraph(all_students, years, "stiinte ale naturii urban boys vs filologie urban boys GPA", export_path, "stiinte ale naturii",
                                                      "filologie", medium='urban', gender="M")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii urban girls vs filologie urban girls GPA", export_path, "stiinte ale naturii",
                                                      "filologie", medium='urban', gender="F")

 create_specialization_linegraph(all_students, years, "stiinte ale naturii vs stiinte sociale GPA", export_path, "stiinte ale naturii", "stiinte sociale")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii rural vs stiinte sociale rural GPA", export_path, "stiinte ale naturii",
                                                      "stiinte sociale", medium='rural')
 create_specialization_linegraph(all_students, years, "stiinte ale naturii rural boys vs stiinte sociale rural boys GPA", export_path, "stiinte ale naturii",
                                                      "stiinte sociale", medium='rural', gender="M")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii rural girls vs rural stiinte sociale rural girls GPA", export_path,
                                                      "stiinte ale naturii","stiinte sociale", medium='rural', gender="F")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii urban vs stiinte sociale urban GPA", export_path, "stiinte ale naturii",
                                                      "stiinte sociale", medium='urban')
 create_specialization_linegraph(all_students, years, "stiinte ale naturii urban boys vs stiinte sociale urban boys GPA", export_path, "stiinte ale naturii",
                                                      "stiinte sociale", medium='urban', gender="M")
 create_specialization_linegraph(all_students, years, "stiinte ale naturii urban girls vs stiinte sociale urban girls GPA", export_path, "stiinte ale naturii",
                                                     "stiinte sociale", medium='urban', gender="F")
 print("Finished creating stiinte ale naturii line graphs\n")

 print("Started creating filologie line graphs")
 create_specialization_linegraph(all_students, years, "filologie vs stiinte sociale GPA", export_path, "filologie", "stiinte sociale")
 create_specialization_linegraph(all_students, years, "filologie rural vs stiinte sociale rural GPA", export_path, "filologie",
                                                      "stiinte sociale", medium='rural')
 create_specialization_linegraph(all_students, years, "filologie rural boys vs stiinte sociale rural boys GPA", export_path, "filologie",
                                                      "stiinte sociale", medium='rural', gender="M")
 create_specialization_linegraph(all_students, years, "filologie rural girls vs rural stiinte sociale rural girls GPA", export_path, "filologie",
                                                      "stiinte sociale", medium='rural', gender="F")
 create_specialization_linegraph(all_students, years, "filologie urban vs stiinte sociale urban GPA", export_path, "filologie",
                                                      "stiinte sociale", medium='urban')
 create_specialization_linegraph(all_students, years, "filologie urban boys vs stiinte sociale urban boys GPA", export_path, "filologie",
                                                      "stiinte sociale", medium='urban', gender="M")
 create_specialization_linegraph(all_students, years, "filologie urban girls vs stiinte sociale urban girls GPA", export_path, "filologie",
                                                      "stiinte sociale", medium='urban', gender="F")
 print("Finished creating filologie line graphs\n")

def create_gender_linegraph(all_students, years, title, export_path,medium=None):
    boys  = {}
    girls = {}
    for year in years:
       boys[year]  = filter_all(all_students[year], gender='M')
       girls[year] = filter_all(all_students[year], gender='F')
    gender_means = get_means(boys, girls, years)
    export_path = os.path.join(export_path, title)
    make_linegraph(gender_means, years, title, export_path, first_category = "Baieti", second_category = "Fete")

def create_medium_linegraph(all_students, years, title, export_path, gender=None):
    rural = {}
    urban = {}
    for year in years:
       urban[year] = filter_all(all_students[year], medium='urban', gender=gender)
       rural[year]  = filter_all(all_students[year], medium='rural', gender=gender)
    medium_means = get_means(rural, urban, years)
    export_path = os.path.join(export_path, title)
    make_linegraph(medium_means, years, title , export_path, first_category = "Rural", second_category = "Urban")

def create_specialization_linegraph(all_students, years, title, export_path, first_spec, second_spec, medium=None, gender=None):
    first = {}
    second = {}
    for year in years:
       temp = filter_all(all_students[year], medium=medium, gender=gender)
       first[year] = filter_all(temp, specialisation=first_spec)
       second[year]  = filter_all(temp, specialisation=second_spec)
    medium_means = get_means(first, second, years)
    export_path = os.path.join(export_path, title)
    make_linegraph(medium_means, years, title, export_path, first_category = first_spec, second_category = second_spec)

def get_grades(students):
    grades = []
    for student in students:
        grades.append(student.final_grade)
    return grades

def get_means(first_category, second_category, years):
    first_grades_means  = []
    second_grades_means = []
    for year in years:
       first_grades_means.append(statistics.mean(get_grades(first_category[year])))
       second_grades_means.append(statistics.mean(get_grades(second_category[year])))
    means = []
    means.append(first_grades_means)
    means.append(second_grades_means)
    return means

if __name__ == "__main__":
    years = ['2015','2016','2017','2019']
    all_students = read_results(years)
    dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    export_path = os.path.join(dirpath,r"plots")
    export_path = os.path.join(export_path, r"Line Graphs")
    create_all_linegraphs(all_students, years, export_path)