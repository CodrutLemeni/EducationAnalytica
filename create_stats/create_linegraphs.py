import statistics
import sys
sys.path.append(r'..')
from filters.student_filters import *
from create_stats.make_linegraph import *

def make_gender_linegraph(all_students, years):
    boys  = {}
    girls = {}
    for year in years:
       boys[year]  = filter_by_gender(all_students[year], 'M')
       girls[year] = filter_by_gender(all_students[year], 'F')
    gender_means = get_means(boys, girls, years)
    make_linegraph(gender_means, years, title = "BAC STATS: GPA VS GENDER", first_category = "Baieti", second_category = "Fete")

def make_medium_linegraph(all_students, years):
    rural = {}
    urban = {}
    for year in years:
       rural[year]  = filter_by_medium(all_students[year], 'rural')
       urban[year] = filter_by_medium(all_students[year], 'urban')
    medium_means = get_means(urban, rural, years)
    make_linegraph(medium_means, years, title = "BAC STATS: GPA VS MEDIUM", first_category = "Urban", second_category = "Rural")
  
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