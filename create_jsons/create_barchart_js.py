import sys
import os
import logging
import numpy as np
import json

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_export_path = os.path.join(dirpath, r"create_jsons")

from filters.student_filters import filter_all
from create_jsons.make_barchart_js import make_barchart_percentage_js
from create_jsons.make_barchart_js import make_barchart_values_js
from create_jsons.make_barchart_js import make_barchart_percentage_subject3_js
from create_jsons.make_barchart_js import make_stacked_barchart_js
from classes.student import initialize_students

from create_stats.make_barchart import make_barchart_percentage


def create_barchart_percentage_js(all_students, current_export_path_js, year):
    # ------procent promovabilitate general fete-baieti--------

    current_export_path_1_js = os.path.join(current_export_path_js, "Fete-Baieti")
    if (os.path.exists(current_export_path_1_js) == False):
        os.mkdir(current_export_path_1_js)
    current_export_path_1_js = os.path.join(current_export_path_1_js, str(year))

    all_students_passed = filter_all(all_students, passed="Promovat")
    all_boys = filter_all(all_students, gender="M")
    all_girls = filter_all(all_students, gender="F")

    all_boys_passed = filter_all(all_students_passed, gender="M")
    all_girls_passed = filter_all(all_students_passed, gender="F")

    students_list = [[len(all_boys)], [len(all_girls)]]
    students_list_passed = [[len(all_boys_passed)], [len(all_girls_passed)]]
    name_list_general = [["Baieti"], ["Fete"]]
    name_list_particular = ["Total"]

    make_barchart_percentage_js(all_categories=students_list, all_categories_good=students_list_passed,
                                categories_general_names=name_list_general,
                                categories_particular_names=name_list_particular,
                                title=("Procentaj promovabilitate Fete - Baieti " + str(year)),
                                current_export_path=current_export_path_1_js,
                                min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}])

    # ------procent promovabilitate toate profilele baieti-fete--------

    current_export_path_2_js = os.path.join(current_export_path_js, "Fete-Baieti mate-info, filo si stiinte")
    if (os.path.exists(current_export_path_2_js) == False):
        os.mkdir(current_export_path_2_js)
    current_export_path2_js = os.path.join(current_export_path_2_js, str(year))

    boys_filo = filter_all(all_students, gender="M", specialisation="filologie")
    boys_filo_passed = filter_all(boys_filo, passed="Promovat")
    girls_filo = filter_all(all_students, gender="F", specialisation="filologie")
    girls_filo_passed = filter_all(girls_filo, passed="Promovat")

    boys_mate_info = filter_all(all_students, gender="M", specialisation="matematica-informatica")
    boys_mate_info_passed = filter_all(boys_mate_info, passed="Promovat")
    girls_mate_info = filter_all(all_students, gender="F", specialisation="matematica-informatica")
    girls_mate_info_passed = filter_all(girls_mate_info, passed="Promovat")

    boys_stiinte = filter_all(all_students, gender="M", specialisation="stiinte ale naturii")
    boys_stiinte_passed = filter_all(boys_stiinte, passed="Promovat")
    girls_stiinte = filter_all(all_students, gender="F", specialisation="stiinte ale naturii")
    girls_stiinte_passed = filter_all(girls_stiinte, passed="Promovat")

    boys_other = filter_all(all_students, gender="M",
                            specialisation_list=["filologie", "matematica-informatica", "stiinte ale naturii"])
    boys_other_passed = filter_all(boys_other, passed="Promovat")
    girls_other = filter_all(all_students, gender="F",
                             specialisation_list=["filologie", "matematica-informatica", "stiinte ale naturii"])
    girls_other_passed = filter_all(girls_other, passed="Promovat")

    boys_list = [len(boys_filo), len(boys_mate_info), len(boys_stiinte), len(boys_other)]
    girls_list = [len(girls_filo), len(girls_mate_info), len(girls_stiinte), len(girls_other)]
    students_list = [boys_list, girls_list]

    boys_list_passed = [len(boys_filo_passed), len(boys_mate_info_passed), len(boys_stiinte_passed),
                        len(boys_other_passed)]
    girls_list_passed = [len(girls_filo_passed), len(girls_mate_info_passed), len(girls_stiinte_passed),
                         len(girls_other_passed)]
    students_list_passed = [boys_list_passed, girls_list_passed]

    name_list_general = [["Baieti"], ["Fete"]]
    name_list_particular = ["Filo", "Mate-info", "Stiinte", "Other"]

    make_barchart_percentage_js(all_categories=students_list, all_categories_good=students_list_passed,
                                categories_general_names=name_list_general,
                                categories_particular_names=name_list_particular, title=(
                    "Procentaj promovabilitate Fete - Baieti \nmate-info, filologie, stiinte ale naturii si restul " + str(
                year)), current_export_path=current_export_path2_js,
                min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}])

    # ------mate-info alegere sub3-------------

    current_export_path_4_js = os.path.join(current_export_path_js, "Alegere subiect mate-info")
    if (os.path.exists(current_export_path_4_js) == False):
        os.mkdir(current_export_path_4_js)
    current_export_path_4_js = os.path.join(current_export_path_4_js, str(year))

    all_students_mate_info = filter_all(all_students, specialisation="matematica-informatica")
    all_students_informatica = filter_all(all_students_mate_info, subject3="informatica mi c/c++")
    all_students_biologie = filter_all(all_students_mate_info, subject3="biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_mate_info,
                                       subject3="anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_mate_info, subject3="chimie organica teo nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_mate_info, subject3="chimie anorganica teo nivel i/ii")
    all_students_fizica = filter_all(all_students_mate_info, subject3="fizica teo")

    students_list = [all_students_informatica, all_students_biologie, all_students_anatomie,
                     all_students_chimie_organica, all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    name_list = ["Informatica", "Biologie", "Anatomie", "Chimie Organica", "Chimie Anorganica", "Fizica"]

    make_barchart_percentage_subject3_js(all_students=students_list, all_grades=all_grades, categories_names=name_list,
                                         title=("Procentaj alegere subiectul III matematica-informatica " + str(year)),
                                         current_export_path=current_export_path_4_js,
                                         min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}, {"suffix":"", "number_precision":2}])

    # ------Stiinte ale naturii alegere sub 3------

    current_export_path_6_js = os.path.join(current_export_path_js, "Alegere subiect stiinte ale naturii")
    if (os.path.exists(current_export_path_6_js) == False):
        os.mkdir(current_export_path_6_js)
    current_export_path_6_js = os.path.join(current_export_path_6_js, str(year))

    all_students_mate_info = filter_all(all_students, specialisation="stiinte ale naturii")
    all_students_informatica = filter_all(all_students_mate_info, subject3="informatica sn c/c++")
    all_students_biologie = filter_all(all_students_mate_info, subject3="biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_mate_info,
                                       subject3="anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_mate_info, subject3="chimie organica teo nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_mate_info, subject3="chimie anorganica teo nivel i/ii")
    all_students_fizica = filter_all(all_students_mate_info, subject3="fizica teo")

    students_list = [all_students_biologie, all_students_anatomie, all_students_informatica,
                     all_students_chimie_organica, all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    name_list = ["Biologie", "Anatomie", "Informatica", "Chimie Organica", "Chimie Anorganica", "Fizica"]

    make_barchart_percentage_subject3_js(all_students=students_list, all_grades=all_grades, categories_names=name_list,
                                         title=("Procentaj alegere subiectul III stiinte ale naturii " + str(year)),
                                         current_export_path=current_export_path_6_js,
                                         min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}, {"suffix":"", "number_precision":2}])

    # ---------Filologie alegere sub3-----------

    current_export_path_5_js = os.path.join(current_export_path_js, "Alegere subiect filologie")
    if (os.path.exists(current_export_path_5_js) == False):
        os.mkdir(current_export_path_5_js)
    current_export_path_5_js = os.path.join(current_export_path_5_js, str(year))

    all_students_filologie = filter_all(all_students, specialisation="filologie")
    all_students_filosofie = filter_all(all_students_filologie, subject3="filosofie")
    all_students_logica = filter_all(all_students_filologie, subject3="logica, argumentare si comunicare")
    all_students_sociologie = filter_all(all_students_filologie, subject3="sociologie")
    all_students_geografie = filter_all(all_students_filologie, subject3="geografie")
    all_students_psihologie = filter_all(all_students_filologie, subject3="psihologie")
    all_students_economie = filter_all(all_students_filologie, subject3="economie")

    students_list = [all_students_filosofie, all_students_logica, all_students_sociologie, all_students_geografie,
                     all_students_psihologie, all_students_economie]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    name_list = ["Filosofie", "Logica", "Sociologie", "Geografie", "Psihologie", "Economie"]

    make_barchart_percentage_subject3_js(all_students=students_list, all_grades=all_grades, categories_names=name_list,
                                         title=("Procentaj alegere subiectul III filologie " + str(year)),
                                         current_export_path=current_export_path_5_js,
                                         min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}, {"suffix":"", "number_precision":2}])
    # ------Profil tehnic alegere sub 3-------------------------

    current_export_path_7_js = os.path.join(current_export_path_js, "Alegere subiect profil Tehnic")
    if (os.path.exists(current_export_path_7_js) == False):
        os.mkdir(current_export_path_7_js)
    current_export_path_7_js = os.path.join(current_export_path_7_js, str(year))

    all_students_tehnic = filter_all(all_students, profile="tehnic")

    # all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica mi c/c++")
    all_students_biologie = filter_all(all_students_tehnic, subject3="biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_tehnic,
                                       subject3="anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_tehnic, subject3="chimie organica teh nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_tehnic, subject3="chimie anorganica teh nivel i/ii")
    all_students_fizica = filter_all(all_students_tehnic, subject3="fizica teh")

    students_list = [all_students_biologie, all_students_anatomie, all_students_chimie_organica,
                     all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    name_list = ["Biologie", "Anatomie", "Chimie Organica", "Chimie Anorganica", "Fizica"]

    make_barchart_percentage_subject3_js(all_students=students_list, all_grades=all_grades, categories_names=name_list,
                                         title=("Procentaj alegere subiectul III Profil Tehnic " + str(year)),
                                         current_export_path=current_export_path_7_js,
                                         min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}, {"suffix":"", "number_precision":2}])

    # ------profil Resurse Naturale alegere sub3----------------

    current_export_path_8_js = os.path.join(current_export_path_js, "Alegere subiect profil Resurse Naturale")
    if (os.path.exists(current_export_path_8_js) == False):
        os.mkdir(current_export_path_8_js)
    current_export_path_8_js = os.path.join(current_export_path_8_js, str(year))

    all_students_resurse = filter_all(all_students, profile="resurse naturale si protectia mediului")

    all_categories = {}
    for i in all_students_resurse:
        all_categories[i.subject3] = "found"

    # all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica mi c/c++")
    all_students_biologie = filter_all(all_students_resurse, subject3="biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_resurse,
                                       subject3="anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_resurse, subject3="chimie organica teh nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_resurse, subject3="chimie anorganica teh nivel i/ii")
    all_students_fizica = filter_all(all_students_resurse, subject3="fizica teh")

    students_list = [all_students_biologie, all_students_anatomie, all_students_chimie_organica,
                     all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    name_list = ["Biologie", "Anatomie", "Chimie Organica", "Chimie Anorganica", "Fizica"]

    make_barchart_percentage_subject3_js(all_students=students_list, all_grades=all_grades, categories_names=name_list,
                                         title=("Procentaj alegere subiectul III Profil Resurse Naturale " + str(year)),
                                         current_export_path=current_export_path_8_js,
                                         min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}, {"suffix":"", "number_precision":2}])

    # ------nota romana mate-info - stiinte ale naturii---------
    mate_info = filter_all(all_students, specialisation="matematica-informatica")
    stiinte = filter_all(all_students, specialisation="stiinte ale naturii")

    grade_mate_info_romana = 0
    grade_stiinte_romana = 0

    for element in mate_info:
        grade_mate_info_romana += element.subject1_grade_final

    for element in stiinte:
        grade_stiinte_romana += element.subject1_grade_final

    current_export_path_3_js = os.path.join(current_export_path_js, "Romana mate-info si stiinte")
    if (os.path.exists(current_export_path_3_js) == False):
        os.mkdir(current_export_path_3_js)
    current_export_path_3_js = os.path.join(current_export_path_3_js, str(year))

    grade_mate_info_romana = float(grade_mate_info_romana) / float(len(mate_info))
    grade_stiinte_romana = float(grade_stiinte_romana) / float(len(stiinte))
    grades = [[grade_mate_info_romana], [grade_stiinte_romana]]
    name_list = ["Mate-info", "Stiinte"]

    make_barchart_values_js(grades, ["mate-info", "stiinte"], ["Nota romana"], "Note romana", current_export_path_3_js,
                            min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[])

    # -----Medie bacalaureat urban-rural------------------------

    urban_students = filter_all(all_students=all_students, medium="urban")
    rural_students = filter_all(all_students=all_students, medium="rural")

    grade_urban = 0
    grade_rural = 0

    for elem in urban_students:
        grade_urban += elem.final_grade
    for elem in rural_students:
        grade_rural += elem.final_grade

    grade_urban /= len(urban_students)
    grade_rural /= len(rural_students)

    current_export_path_13_js = os.path.join(current_export_path_js, "Medie Bacalaureat Urban-Rural")
    if (os.path.exists(current_export_path_13_js) == False):
        os.mkdir(current_export_path_13_js)
    current_export_path_13_js = os.path.join(current_export_path_13_js, str(year))

    grades = [[grade_urban], [grade_rural]]

    make_barchart_values_js(grades, ["Urban", "Rural"], ["Medie Bacalaureat"], "Medie Bacalaureat",
                            current_export_path_13_js,
                            min_val=0, max_val=10, suffix="", number_precision=2, extra_formats=[])

    # ----Medie bacalaureat urban-rural fete-baieti---------

    current_export_path_14_js = os.path.join(current_export_path_js, "Medie Bacalaureat Urban-Rural Fete-Baieti")
    if (os.path.exists(current_export_path_14_js) == False):
        os.mkdir(current_export_path_14_js)
    current_export_path_14_js = os.path.join(current_export_path_14_js, str(year))

    urban_students = filter_all(all_students=all_students, medium="urban")
    rural_students = filter_all(all_students=all_students, medium="rural")

    urban_girls = filter_all(all_students=urban_students, gender="F")
    urban_boys = filter_all(all_students=urban_students, gender="M")

    rural_girls = filter_all(all_students=rural_students, gender="F")
    rural_boys = filter_all(all_students=rural_students, gender="M")

    grade_urban_girls = 0
    grade_rural_girls = 0
    grade_urban_boys = 0
    grade_rural_boys = 0

    for elem in urban_girls:
        grade_urban_girls += elem.final_grade
    for elem in rural_girls:
        grade_rural_girls += elem.final_grade
    for elem in urban_boys:
        grade_urban_boys += elem.final_grade
    for elem in rural_boys:
        grade_rural_boys += elem.final_grade

    grade_urban_girls /= len(urban_girls)
    grade_rural_girls /= len(rural_girls)
    grade_urban_boys /= len(urban_boys)
    grade_rural_boys /= len(rural_boys)

    grades = [[grade_urban_girls, grade_urban_boys], [grade_rural_girls, grade_rural_boys]]

    make_barchart_values_js(grades, ["Urban", "Rural"], ["Medie Bacalaureat Fete", "Medie Bacalaureat Baieti"],
                            "Medie Bacalaureat Urban-Rural Fete-Baieti", current_export_path_14_js,
                            min_val=0, max_val=10, suffix="", number_precision=2, extra_formats=[])

    # -------Medie bacalaureat pe profile-----------------------

    current_export_path_15_js = os.path.join(current_export_path_js, "Medie Bacalaureat pe Profile")
    if (os.path.exists(current_export_path_15_js) == False):
        os.mkdir(current_export_path_15_js)
    current_export_path_15_js = os.path.join(current_export_path_15_js, str(year))

    mate_info_students = filter_all(all_students=all_students, specialisation="matematica-informatica")
    stiinte_students = filter_all(all_students=all_students, specialisation="stiinte ale naturii")
    filo_studentts = filter_all(all_students=all_students, specialisation="filologie")

    grade_mate_info = 0
    grade_filo = 0
    grade_stiinte = 0

    for elem in mate_info_students:
        grade_mate_info += elem.final_grade
    for elem in filo_studentts:
        grade_filo += elem.final_grade
    for elem in stiinte_students:
        grade_stiinte += elem.final_grade

    grade_filo /= len(filo_studentts)
    grade_mate_info /= len(mate_info_students)
    grade_stiinte /= len(stiinte_students)

    grades = [[grade_filo], [grade_mate_info], [grade_stiinte]]

    make_barchart_values_js(grades, ["Filologie", "Matematica-Informatica", "Stiinte ale Naturii"],
                            ["Medie Bacalaureat"], "Medie Bacalaureat pe Profile", current_export_path_15_js,
                             min_val=0, max_val=10, suffix="", number_precision=2, extra_formats=[])

    # -----procentaj promovabilitate urban-rural----------------

    current_export_path_9_js = os.path.join(current_export_path_js, "Procentaj Promovabilitate urban-rural")
    if (os.path.exists(current_export_path_9_js) == False):
        os.mkdir(current_export_path_9_js)
    current_export_path_9_js = os.path.join(current_export_path_9_js, str(year))

    all_students_passed = filter_all(all_students, passed="Promovat")

    all_students_urban = filter_all(all_students=all_students, medium="urban")
    all_students_urban_passed = filter_all(all_students=all_students_passed, medium="urban")
    all_students_rural = filter_all(all_students=all_students, medium="rural")
    all_students_rural_passed = filter_all(all_students=all_students_passed, medium="rural")

    categories_general_names = [["Urban"], ["Rural"]]
    categories_particular_names = ["Total"]
    all_students_list = [[len(all_students_urban)], [len(all_students_rural)]]
    all_students_passed_list = [[len(all_students_urban_passed)], [len(all_students_rural_passed)]]

    make_barchart_percentage_js(all_categories=all_students_list, all_categories_good=all_students_passed_list,
                                categories_general_names=categories_general_names,
                                categories_particular_names=categories_particular_names,
                                title=("Procentaj Promovabilitate urban-rural" + str(year)),
                                current_export_path=current_export_path_9_js,
                                min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}])
    # make_barchart_percentage(all_categories = all_students_list, all_categories_good = all_students_passed_list, categories_names = name_list, title = ("Procentaj Promovabilitate urban-rural " + str(year)), current_export_path = current_export_path_9_js, colors = ['#F4DADA', '#BEEBE9'])

    # -----procentaj promovabilitate fete-baieti urban-rural------------

    current_export_path_10_js = os.path.join(current_export_path_js,
                                             "Procentaj Promovabilitate fete-baieti urban-rural")
    if (os.path.exists(current_export_path_10_js) == False):
        os.mkdir(current_export_path_10_js)
    current_export_path_10_js = os.path.join(current_export_path_10_js, str(year))

    all_students_passed = filter_all(all_students, passed="Promovat")

    all_students_urban = filter_all(all_students=all_students, medium="urban")
    all_students_urban_boys = filter_all(all_students=all_students_urban, gender="M")
    all_students_urban_girls = filter_all(all_students=all_students_urban, gender="F")
    all_students_urban_passed = filter_all(all_students=all_students_passed, medium="urban")
    all_students_urban_boys_passed = filter_all(all_students=all_students_urban_passed, gender="M")
    all_students_urban_girls_passed = filter_all(all_students=all_students_urban_passed, gender="F")
    all_students_rural = filter_all(all_students=all_students, medium="rural")
    all_students_rural_boys = filter_all(all_students=all_students_rural, gender="M")
    all_students_rural_girls = filter_all(all_students=all_students_rural, gender="F")
    all_students_rural_passed = filter_all(all_students=all_students_passed, medium="rural")
    all_students_rural_boys_passed = filter_all(all_students=all_students_rural_passed, gender="M")
    all_students_rural_girls_passed = filter_all(all_students=all_students_rural_passed, gender="F")

    name_list = ["Baieti-Urban", "Fete-Urban", "Baieti-Rural", "Fete-Rural"]
    all_students_list = [[len(all_students_urban_boys), len(all_students_rural_boys)],
                         [len(all_students_urban_girls), len(all_students_rural_girls)]]
    all_students_passed_list = [[len(all_students_urban_boys_passed), len(all_students_rural_boys_passed)],
                                [len(all_students_urban_girls_passed), len(all_students_rural_girls_passed)]]
    categories_general_names = [["Baieti"], ["Fete"]]
    categories_particular_names = ["Urban", "Rural"]

    make_barchart_percentage_js(all_categories=all_students_list, all_categories_good=all_students_passed_list,
                                categories_general_names=categories_general_names,
                                categories_particular_names=categories_particular_names,
                                title=("Procentaj Promovabilitate urban-rural" + str(year)),
                                current_export_path=current_export_path_10_js,
                                min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}])
    # make_barchart_percentage(all_categories = all_students_list, all_categories_good = all_students_passed_list, categories_names = name_list, title = ("Procentaj Promovabilitate fete-baieti urban-rural " + str(year)), current_export_path = current_export_path_10_js, colors = ['#F4DADA', '#BEEBE9'])

    # -------procentaj alegere profil in functie de mediu de viata-----------------

    current_export_path_11_js = os.path.join(current_export_path_js,
                                             "Procentaj alegere profil in functie de mediu de viata")
    if (os.path.exists(current_export_path_11_js) == False):
        os.mkdir(current_export_path_11_js)
    current_export_path_11_js = os.path.join(current_export_path_11_js, str(year))

    urban_filo = filter_all(all_students, medium="urban", specialisation="filologie")
    rural_filo = filter_all(all_students, medium="rural", specialisation="filologie")
    urban_mate_info = filter_all(all_students, medium="urban", specialisation="matematica-informatica")
    rural_mate_info = filter_all(all_students, medium="rural", specialisation="matematica-informatica")
    urban_stiinte = filter_all(all_students, medium="urban", specialisation="stiinte ale naturii")
    rural_stiinte = filter_all(all_students, medium="rural", specialisation="stiinte ale naturii")
    urban_other = filter_all(all_students, medium="urban",
                             specialisation_list=["filologie", "matematica-informatica", "stiinte ale naturii"])
    rural_other = filter_all(all_students, medium="rural",
                             specialisation_list=["filologie", "matematica-informatica", "stiinte ale naturii"])

    urban_stats = [len(urban_filo), len(urban_mate_info), len(urban_stiinte), len(urban_other)]
    rural_stats = [len(rural_filo), len(rural_mate_info), len(rural_stiinte), len(rural_other)]

    vertical_names = ["Urban", "Rural"]
    horizontal_names = ["Filo", "Mate_info", "Stiinte", "Other"]

    all_categories = [urban_stats, rural_stats]

    make_stacked_barchart_js(all_categories=all_categories, vertical_names=vertical_names,
                             horizontal_names=horizontal_names,
                             title=("Procentaj alegere profil in functie de sex" + str(year)),
                             current_export_path=current_export_path_11_js,
                             min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}])

    # -----procentaj alegere profil in functie de sex---------------------------

    current_export_path_12_js = os.path.join(current_export_path_js, "Procentaj alegere profil in functie de sex")
    if (os.path.exists(current_export_path_12_js) == False):
        os.mkdir(current_export_path_12_js)
    current_export_path_12_js = os.path.join(current_export_path_12_js, str(year))

    boys_filo = filter_all(all_students, gender="M", specialisation="filologie")
    girls_filo = filter_all(all_students, gender="F", specialisation="filologie")

    boys_mate_info = filter_all(all_students, gender="M", specialisation="matematica-informatica")
    girls_mate_info = filter_all(all_students, gender="F", specialisation="matematica-informatica")

    boys_stiinte = filter_all(all_students, gender="M", specialisation="stiinte ale naturii")
    girls_stiinte = filter_all(all_students, gender="F", specialisation="stiinte ale naturii")

    boys_other = filter_all(all_students, gender="M",
                            specialisation_list=["filologie", "matematica-informatica", "stiinte ale naturii"])
    girls_other = filter_all(all_students, gender="F",
                             specialisation_list=["filologie", "matematica-informatica", "stiinte ale naturii"])

    urban_stats = [len(boys_filo), len(boys_mate_info), len(boys_stiinte), len(boys_other)]
    rural_stats = [len(girls_filo), len(girls_mate_info), len(girls_stiinte), len(girls_other)]

    vertical_names = ["Baieti", "Fete"]
    horizontal_names = ["Filo", "Mate_info", "Stiinte", "Other"]

    all_categories = [urban_stats, rural_stats]

    make_stacked_barchart_js(all_categories=all_categories, vertical_names=vertical_names,
                             horizontal_names=horizontal_names,
                             title=("Procentaj alegere profil in functie de sex" + str(year)),
                             current_export_path=current_export_path_12_js,
                             min_val=0, max_val=100, suffix="%", number_precision=2, extra_formats=[{"suffix":"", "number_precision":0}])


if __name__ == "__main__":
    base_path = os.path.join(dirpath, r"data")
    for year in range(2015, 2020):
        try:
            csv_path = os.path.join(base_path, "good_bac_" + str(year) + ".csv")
            all_students = initialize_students(csv_path)
            current_export_path_js = os.path.join(json_export_path, "Horizontal Bar Charts")
            if (os.path.exists(current_export_path_js) == False):
                os.mkdir(current_export_path_js)
            create_barchart_percentage_js(all_students=all_students, current_export_path_js=current_export_path_js,
                                          year=year)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            print(f"Year {year} went wrong")
