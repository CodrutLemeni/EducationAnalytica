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

    specialisation_comparison_graph(all_students, years, "3 specs general comparison", "matematica-informatica",
        "stiinte ale naturii", "filologie", export_path)
    specialisation_comparison_graph(all_students, years, "3 specs general comparison_1", "matematica-informatica",
        "stiinte ale naturii", "stiinte sociale", export_path)
    specialisation_comparison_graph(all_students, years, "3 specs general comparison_2", "stiinte sociale",
        "stiinte ale naturii", "filologie", export_path)
    specialisation_comparison_graph(all_students, years, "3 specs general comparison_3", "matematica-informatica",
        "stiinte sociale", "filologie", export_path)

    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_boys", "matematica-informatica", "stiinte ale naturii", "filologie",
    #                                                     export_path, gender='M')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_1_boys", "matematica-informatica", "stiinte ale naturii", "stiinte sociale",
    #                                                     export_path, gender = 'M')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_2_boys", "stiinte sociale", "stiinte ale naturii", "filologie", 
    #                                                     export_path, gender = 'M')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_3_boys", "matematica-informatica", "stiinte sociale", "filologie",
    #                                                     export_path, gender = 'M')

    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_girls", "matematica-informatica", "stiinte ale naturii", "filologie",
    #                                                     export_path, gender='F')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_1_girls", "matematica-informatica", "stiinte ale naturii", "stiinte sociale",
    #                                                     export_path, gender = 'F')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_2_girls", "stiinte sociale", "stiinte ale naturii", "filologie", 
    #                                                     export_path, gender = 'F')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_3_girls", "matematica-informatica", "stiinte sociale", "filologie",
    #                                                     export_path, gender = 'F')

    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_urban", "matematica-informatica", "stiinte ale naturii", "filologie",
    #                                                     export_path, medium='urban')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_1_urban", "matematica-informatica", "stiinte ale naturii", "stiinte sociale",
    #                                                     export_path, medium = 'urban')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_2_urban", "stiinte sociale", "stiinte ale naturii", "filologie", 
    #                                                     export_path, medium = 'urban')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_3_urban", "matematica-informatica", "stiinte sociale", "filologie",
    #                                                     export_path, medium = 'urban')

    # specialisation_comparison_graph(all_students, years, "3 specs general rural", "matematica-informatica", "stiinte ale naturii", "filologie",
    #                                                     export_path, medium='rural')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_1_rural", "matematica-informatica", "stiinte ale naturii", "stiinte sociale",
    #                                                     export_path, medium = 'rural')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_2_rural", "stiinte sociale", "stiinte ale naturii", "filologie", 
    #                                                     export_path, medium = 'rural')
    # specialisation_comparison_graph(all_students, years, "3 specs general comparison_3_rural", "matematica-informatica", "stiinte sociale", "filologie",
    #                                                     export_path, medium = 'rural')


    # print("Started creating mate-info line graphs")
    # create_specialization_linegraph(all_students, years, "mate-info vs stiinte ale naturii GPA", export_path, "matematica-informatica", "stiinte ale naturii")
    # create_specialization_linegraph(all_students, years, "mate-info rural vs stiinte ale naturii rural GPA", export_path, "matematica-informatica",
    #                                                     "stiinte ale naturii", medium='rural')
    # create_specialization_linegraph(all_students, years, "mate-info rural boys vs stiinte ale naturii rural boys GPA", export_path, "matematica-informatica",
    #                                                     "stiinte ale naturii", medium='rural', gender="M")
    # create_specialization_linegraph(all_students, years, "mate-info rural girls vs rural stiinte ale naturii rural girls GPA", export_path,
    #                                                     "matematica-informatica","stiinte ale naturii", medium='rural', gender="F")
    # create_specialization_linegraph(all_students, years, "mate-info urban vs stiinte ale naturii urban GPA", export_path, "matematica-informatica",
    #                                                     "stiinte ale naturii", medium='urban')
    # create_specialization_linegraph(all_students, years, "mate-info urban boys vs stiinte ale naturii urban boys GPA", export_path, "matematica-informatica",
    #                                                     "stiinte ale naturii", medium='urban', gender="M")
    # create_specialization_linegraph(all_students, years, "mate-info urban girls vs stiinte ale naturii urban girls GPA", export_path, "matematica-informatica",
    #                                                     "stiinte ale naturii", medium='urban', gender="F")
    # create_specialization_linegraph(all_students, years, "mate-info vs filologie GPA", export_path, "matematica-informatica", "filologie")
    # create_specialization_linegraph(all_students, years, "mate-info rural vs filologie rural GPA", export_path, "matematica-informatica",
    #                                                     "filologie", medium='rural')
    # create_specialization_linegraph(all_students, years, "mate-info rural boys vs filologie rural boys GPA", export_path, "matematica-informatica",
    #                                                     "filologie", medium='rural', gender="M")
    # create_specialization_linegraph(all_students, years, "mate-info rural girls vs rural filologie rural girls GPA", export_path, "matematica-informatica",
    #                                                     "filologie", medium='rural', gender="F")
    # create_specialization_linegraph(all_students, years, "mate-info urban vs filologie urban GPA", export_path, "matematica-informatica",
    #                                                     "filologie", medium='urban')
    # create_specialization_linegraph(all_students, years, "mate-info urban boys vs filologie urban boys GPA", export_path, "matematica-informatica",
    #                                                     "filologie", medium='urban', gender="M")
    # create_specialization_linegraph(all_students, years, "mate-info urban girls vs filologie urban girls GPA", export_path, "matematica-informatica",
    #                                                     "filologie", medium='urban', gender="F")
    # create_specialization_linegraph(all_students, years, "mate-info vs stiinte sociale GPA", export_path, "matematica-informatica", "stiinte sociale")
    # create_specialization_linegraph(all_students, years, "mate-info rural vs stiinte sociale rural GPA", export_path, "matematica-informatica",
    #                                                     "stiinte sociale", medium='rural')
    # create_specialization_linegraph(all_students, years, "mate-info rural boys vs stiinte sociale rural boys GPA", export_path, "matematica-informatica",
    #                                                     "stiinte sociale", medium='rural', gender="M")
    # create_specialization_linegraph(all_students, years, "mate-info rural girls vs rural stiinte sociale rural girls GPA", export_path, "matematica-informatica",
    #                                                     "stiinte sociale", medium='rural', gender="F")
    # create_specialization_linegraph(all_students, years, "mate-info urban vs stiinte sociale urban GPA", export_path, "matematica-informatica",
    #                                                     "stiinte sociale", medium='urban')
    # create_specialization_linegraph(all_students, years, "mate-info urban boys vs stiinte sociale urban boys GPA", export_path, "matematica-informatica",
    #                                                     "stiinte sociale", medium='urban', gender="M")
    # create_specialization_linegraph(all_students, years, "mate-info urban girls vs stiinte sociale urban girls GPA", export_path, "matematica-informatica",
    #                                                     "stiinte sociale", medium='urban', gender="F")
    # print("Finished creating mate-info line graphs\n")

    # print("Started creating stiinte ale naturii line graphs")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii vs filologie GPA", export_path, "stiinte ale naturii", "filologie")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii rural vs filologie rural GPA", export_path, "stiinte ale naturii",
    #                                                     "filologie", medium='rural')
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii rural boys vs filologie rural boys GPA", export_path, "stiinte ale naturii",
    #                                                     "filologie", medium='rural', gender="M")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii rural girls vs rural filologie rural girls GPA", export_path, "stiinte ale naturii",
    #                                                     "filologie", medium='rural', gender="F")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii urban vs filologie urban GPA", export_path, "stiinte ale naturii",
    #                                                     "filologie", medium='urban')
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii urban boys vs filologie urban boys GPA", export_path, "stiinte ale naturii",
    #                                                     "filologie", medium='urban', gender="M")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii urban girls vs filologie urban girls GPA", export_path, "stiinte ale naturii",
    #                                                     "filologie", medium='urban', gender="F")

    # create_specialization_linegraph(all_students, years, "stiinte ale naturii vs stiinte sociale GPA", export_path, "stiinte ale naturii", "stiinte sociale")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii rural vs stiinte sociale rural GPA", export_path, "stiinte ale naturii",
    #                                                     "stiinte sociale", medium='rural')
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii rural boys vs stiinte sociale rural boys GPA", export_path, "stiinte ale naturii",
    #                                                     "stiinte sociale", medium='rural', gender="M")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii rural girls vs rural stiinte sociale rural girls GPA", export_path,
    #                                                     "stiinte ale naturii","stiinte sociale", medium='rural', gender="F")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii urban vs stiinte sociale urban GPA", export_path, "stiinte ale naturii",
    #                                                     "stiinte sociale", medium='urban')
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii urban boys vs stiinte sociale urban boys GPA", export_path, "stiinte ale naturii",
    #                                                     "stiinte sociale", medium='urban', gender="M")
    # create_specialization_linegraph(all_students, years, "stiinte ale naturii urban girls vs stiinte sociale urban girls GPA", export_path, "stiinte ale naturii",
    #                                                     "stiinte sociale", medium='urban', gender="F")
    # print("Finished creating stiinte ale naturii line graphs\n")

    # print("Started creating filologie line graphs")
    # create_specialization_linegraph(all_students, years, "filologie vs stiinte sociale GPA", export_path, "filologie", "stiinte sociale")
    # create_specialization_linegraph(all_students, years, "filologie rural vs stiinte sociale rural GPA", export_path, "filologie",
    #                                                     "stiinte sociale", medium='rural')
    # create_specialization_linegraph(all_students, years, "filologie rural boys vs stiinte sociale rural boys GPA", export_path, "filologie",
    #                                                     "stiinte sociale", medium='rural', gender="M")
    # create_specialization_linegraph(all_students, years, "filologie rural girls vs rural stiinte sociale rural girls GPA", export_path, "filologie",
    #                                                     "stiinte sociale", medium='rural', gender="F")
    # create_specialization_linegraph(all_students, years, "filologie urban vs stiinte sociale urban GPA", export_path, "filologie",
    #                                                     "stiinte sociale", medium='urban')
    # create_specialization_linegraph(all_students, years, "filologie urban boys vs stiinte sociale urban boys GPA", export_path, "filologie",
    #                                                     "stiinte sociale", medium='urban', gender="M")
    # create_specialization_linegraph(all_students, years, "filologie urban girls vs stiinte sociale urban girls GPA", export_path, "filologie",
    #                                                     "stiinte sociale", medium='urban', gender="F")
    # print("Finished creating filologie line graphs\n")

def specialisation_comparison_graph(all_students, years, title, specialisation_1, specialisation_2, specialisation_3, export_path,
                                    gender=None, medium=None):
    spec_1 = {}
    spec_2 = {}
    spec_3 = {}
    for year in years:
        spec_1[year] = filter_all(all_students[year], specialisation = specialisation_1, gender=gender, medium=medium)
        spec_2[year] = filter_all(all_students[year], specialisation = specialisation_2, gender=gender, medium=medium)
        spec_3[year] = filter_all(all_students[year], specialisation = specialisation_3, gender=gender, medium=medium)
    all_specs_means = get_means([spec_1, spec_2, spec_3], years)
    limits = min_max_mean([spec_1, spec_2, spec_3])
    export_path = os.path.join(export_path, title)
    make_linegraph(all_specs_means, years, title, export_path, limits=limits, categories=[specialisation_1, specialisation_2, specialisation_3])

def create_gender_linegraph(all_students, years, title, export_path,medium=None):
    boys  = {}
    girls = {}
    for year in years:
       boys[year]  = filter_all(all_students[year], gender='M', medium = medium)
       girls[year] = filter_all(all_students[year], gender='F', medium = medium)
    gender_means = get_means([boys, girls], years)
    export_path = os.path.join(export_path, title)
    make_linegraph(gender_means, years, title, export_path, categories=["Baieti", "Fete"])

def create_medium_linegraph(all_students, years, title, export_path, gender=None):
    rural = {}
    urban = {}
    for year in years:
       urban[year] = filter_all(all_students[year], medium='urban', gender=gender)
       rural[year]  = filter_all(all_students[year], medium='rural', gender=gender)
    medium_means = get_means([rural, urban], years)
    export_path = os.path.join(export_path, title)
    make_linegraph(medium_means, years, title , export_path, categories=["Rural", "Urban"])

def create_specialization_linegraph(all_students, years, title, export_path, first_spec, second_spec, medium=None, gender=None):
    first = {}
    second = {}
    for year in years:
       temp = filter_all(all_students[year], medium=medium, gender=gender)
       first[year] = filter_all(temp, specialisation=first_spec)
       second[year]  = filter_all(temp, specialisation=second_spec)
    medium_means = get_means([first, second], years)
    export_path = os.path.join(export_path, title)
    make_linegraph(medium_means, years, title, export_path, categories=[first_spec, second_spec])

def get_grades(students):
    grades = []
    for student in students:
        grades.append(student.final_grade)
    return grades

def get_means(students, years):
    '''
        function takes a list of dictionaries(students) which has
        every year in years as a key and the value for each key is
        a list of grades

        it returns the mean for each of the category(key) in the dictionary, for each year
    '''
    grades = [[] for s in students]
    i = 0
    for l in students:
        for year in years:
            grades[i].append(statistics.mean(get_grades(l[year])))
        i += 1
    return grades

def min_max_mean(students):
    '''
        function returns the limits
    '''
    minimum = 10
    maximum = 0
    for dict_s in students:
        for l in dict_s.values():
            minimum = min(minimum, statistics.mean(get_grades(l)))
            maximum = max(maximum, statistics.mean(get_grades(l)))
    return [minimum-0.5, maximum+0.5]

if __name__ == "__main__":
    years = ['2015','2016','2017','2019']
    all_students = read_results(years)
    dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    export_path = os.path.join(dirpath,r"plots")
    export_path = os.path.join(export_path, r"Line Graphs")
    create_all_linegraphs(all_students, years, export_path)