import os
import sys

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

from filters.student_filters import filter_all
from create_stats.make_barchart import make_barchart_percentage
from create_stats.make_barchart import make_barchart_values
from create_stats.make_barchart import make_barchart_percentage_subject3
from create_stats.make_barchart_js import make_barchart_percentage_js
from create_stats.make_barchart_js import make_barchart_values_js
from create_stats.make_barchart_js import make_barchart_percentage_subject3_js

def create_barchart_percentage(all_students, current_export_path, current_export_path_js, year):

    #------procent promovabilitate general fete-baieti--------
    current_export_path_1 = os.path.join(current_export_path, "Fete-Baieti")
    if( os.path.exists(current_export_path_1) == False):
        os.mkdir(current_export_path_1)
    current_export_path_1_js = os.path.join(current_export_path_js, "Fete-Baieti")

    current_export_path_1 = os.path.join(current_export_path_1, str(year))
    if( os.path.exists(current_export_path_1_js) == False):
        os.mkdir(current_export_path_1_js)
    current_export_path_1_js = os.path.join(current_export_path_1_js, str(year))

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
    make_barchart_percentage_js(all_categories = students_list, all_categories_good = students_list_passed, categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti " + str(year)), current_export_path = current_export_path_1_js, colors = colors)
    
    #------procent promovabilitate toate profilele baieti-fete--------
    
    current_export_path_2 = os.path.join(current_export_path, "Fete-Baieti mate-info, filo si stiinte")
    if( os.path.exists(current_export_path_2) == False):
        os.mkdir(current_export_path_2)
    current_export_path2 = os.path.join(current_export_path_2, str(year))

    current_export_path_2_js = os.path.join(current_export_path_js, "Fete-Baieti mate-info, filo si stiinte")
    if( os.path.exists(current_export_path_2_js) == False):
        os.mkdir(current_export_path_2_js)
    current_export_path2_js = os.path.join(current_export_path_2_js, str(year))

    boys_filo = filter_all(all_students, gender="M", specialisation="filologie")
    girls_filo = filter_all(all_students, gender="F", specialisation="filologie")
    boys_mate_info = filter_all(all_students, gender="M", specialisation="matematica-informatica")
    girls_mate_info = filter_all(all_students, gender="F", specialisation="matematica-informatica")
    boys_stiinte = filter_all(all_students, gender="M", specialisation="stiinte ale naturii")
    girls_stiinte = filter_all(all_students, gender="F", specialisation="stiinte ale naturii")
    boys_other = filter_all(all_students, gender="M", specialisation_list = ["filologie", "matematica-informatica", "stiinte ale naturii"])
    girls_other = filter_all(all_students, gender="F", specialisation_list = ["filologie", "matematica-informatica", "stiinte ale naturii"])
    colors = ['#BEEBE9', '#F4DADA', '#BEEBE9', '#F4DADA', '#BEEBE9', '#F4DADA', '#BEEBE9', '#F4DADA']

    students_list = [boys_other, girls_other, boys_filo, girls_filo, boys_mate_info, girls_mate_info, boys_stiinte, girls_stiinte]
    name_list = ["Baitei other", "Fete other", "Baieti filologie",  "Fete filologie", "Baieti mate-info", "Fete mate-info", "Baieti stiinte", "Fete stiinte"]
    
    students_list_passed = []

    for crt_student_list in students_list:
        students_list_passed.append(filter_all(crt_student_list,passed = "Promovat"))
    
    make_barchart_percentage(all_categories = students_list, all_categories_good = students_list_passed,categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti \nmate-info, filologie, stiinte ale naturii si restul " + str(year)), current_export_path = current_export_path2, colors = colors)
    make_barchart_percentage_js(all_categories = students_list, all_categories_good = students_list_passed,categories_names = name_list, title = ("Procentaj promovabilitate Fete - Baieti \nmate-info, filologie, stiinte ale naturii si restul " + str(year)), current_export_path = current_export_path2_js, colors = colors)

    #------mate-info alegere sub3-------------
    current_export_path_4 = os.path.join(current_export_path, "Alegere subiect mate-info")
    if( os.path.exists(current_export_path_4) == False):
        os.mkdir(current_export_path_4)
    current_export_path_4 = os.path.join(current_export_path_4, str(year))

    current_export_path_4_js = os.path.join(current_export_path_js, "Alegere subiect mate-info")
    if( os.path.exists(current_export_path_4_js) == False):
        os.mkdir(current_export_path_4_js)
    current_export_path_4_js = os.path.join(current_export_path_4_js, str(year))

    all_students_mate_info = filter_all(all_students, specialisation = "matematica-informatica")
    all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica mi c/c++")
    all_students_biologie = filter_all(all_students_mate_info, subject3 = "biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_mate_info, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_mate_info, subject3 = "chimie organica teo nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_mate_info, subject3 = "chimie anorganica teo nivel i/ii")
    all_students_fizica = filter_all(all_students_mate_info, subject3 = "fizica teo")
    

    students_list = [all_students_informatica, all_students_biologie, all_students_anatomie, all_students_chimie_organica, all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B3C7BA', '#B28B90']


    name_list = ["Informatica", "Biologie", "Anatomie",  "Chimie Organica", "Chimie Anorganica", "Fizica"]
    make_barchart_percentage_subject3(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III matematica-informatica " + str(year)), current_export_path = current_export_path_4, colors = colors)
    make_barchart_percentage_subject3_js(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III matematica-informatica " + str(year)), current_export_path = current_export_path_4_js, colors = colors)

    #------Stiinte ale naturii alegere sub 3------
    current_export_path_6 = os.path.join(current_export_path, "Alegere subiect stiinte ale naturii")
    if( os.path.exists(current_export_path_6) == False):
        os.mkdir(current_export_path_6)
    current_export_path_6 = os.path.join(current_export_path_6, str(year))
    
    current_export_path_6_js = os.path.join(current_export_path_js, "Alegere subiect stiinte ale naturii") 
    if( os.path.exists(current_export_path_6_js) == False):
        os.mkdir(current_export_path_6_js)
    current_export_path_6_js = os.path.join(current_export_path_6_js, str(year))

    all_students_mate_info = filter_all(all_students, specialisation = "stiinte ale naturii")
    all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica sn c/c++")
    all_students_biologie = filter_all(all_students_mate_info, subject3 = "biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_mate_info, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_mate_info, subject3 = "chimie organica teo nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_mate_info, subject3 = "chimie anorganica teo nivel i/ii")
    all_students_fizica = filter_all(all_students_mate_info, subject3 = "fizica teo")
    

    students_list = [all_students_biologie, all_students_anatomie, all_students_informatica, all_students_chimie_organica, all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#658763', '#B28B90']

    
    name_list = ["Biologie", "Anatomie",  "Informatica", "Chimie Organica", "Chimie Anorganica", "Fizica"]
    
    make_barchart_percentage_subject3(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III stiinte ale naturii " + str(year)), current_export_path = current_export_path_6, colors = colors)
    make_barchart_percentage_subject3_js(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III stiinte ale naturii " + str(year)), current_export_path = current_export_path_6_js, colors = colors)


    #---------Filologie alegere sub3-----------
    current_export_path_5 = os.path.join(current_export_path, "Alegere subiect filologie")
    if( os.path.exists(current_export_path_5) == False):
        os.mkdir(current_export_path_5)
    current_export_path_5 = os.path.join(current_export_path_5, str(year))

    current_export_path_5_js = os.path.join(current_export_path_js, "Alegere subiect filologie")
    if( os.path.exists(current_export_path_5_js) == False):
        os.mkdir(current_export_path_5_js)
    current_export_path_5_js = os.path.join(current_export_path_5_js, str(year))

    all_students_filologie = filter_all(all_students, specialisation = "filologie")
    all_students_filosofie = filter_all(all_students_filologie, subject3 = "filosofie")
    all_students_logica = filter_all(all_students_filologie, subject3 = "logica, argumentare si comunicare")
    all_students_sociologie = filter_all(all_students_filologie, subject3 = "sociologie")
    all_students_geografie = filter_all(all_students_filologie, subject3 = "geografie")
    all_students_psihologie = filter_all(all_students_filologie, subject3 = "psihologie")
    all_students_economie = filter_all(all_students_filologie, subject3="economie")
    

    students_list = [all_students_filosofie, all_students_logica, all_students_sociologie, all_students_geografie, all_students_psihologie, all_students_economie]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B3C7BA', '#658763']

    
    name_list = ["Filosofie", "Logica", "Sociologie",  "Geografie", "Psihologie", "Economie"]

    make_barchart_percentage_subject3(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III filologie " + str(year)), current_export_path = current_export_path_5, colors = colors)
    make_barchart_percentage_subject3_js(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III filologie " + str(year)), current_export_path = current_export_path_5_js, colors = colors)

    #------Profil tehnic alegere sub 3-------------------------

    current_export_path_7 = os.path.join(current_export_path, "Alegere subiect profil Tehnic")
    if( os.path.exists(current_export_path_7) == False):
        os.mkdir(current_export_path_7)
    current_export_path_7 = os.path.join(current_export_path_7, str(year))

    current_export_path_7_js = os.path.join(current_export_path_js, "Alegere subiect profil Tehnic")
    if( os.path.exists(current_export_path_7_js) == False):
        os.mkdir(current_export_path_7_js)
    current_export_path_7_js = os.path.join(current_export_path_7_js, str(year))
    
    all_students_tehnic = filter_all(all_students, profile = "tehnic")

    
    
    #all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica mi c/c++")
    all_students_biologie = filter_all(all_students_tehnic, subject3 = "biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_tehnic, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_tehnic, subject3 = "chimie organica teh nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_tehnic, subject3="chimie anorganica teh nivel i/ii")
    all_students_fizica = filter_all(all_students_tehnic, subject3 = "fizica teh")
    

    students_list = [all_students_biologie, all_students_anatomie, all_students_chimie_organica, all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B28B90']

    
    name_list = ["Biologie", "Anatomie",  "Chimie Organica", "Chimie Anorganica", "Fizica"]
    
    make_barchart_percentage_subject3(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III Profil Tehnic " + str(year)), current_export_path = current_export_path_7, colors = colors)
    make_barchart_percentage_subject3_js(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III Profil Tehnic " + str(year)), current_export_path = current_export_path_7_js, colors = colors)


    #------profil Resurse Naturale alegere sub3----------------

    current_export_path_8 = os.path.join(current_export_path, "Alegere subiect profil Resurse Naturale")
    if( os.path.exists(current_export_path_8) == False):
        os.mkdir(current_export_path_8)
    current_export_path_8 = os.path.join(current_export_path_8, str(year))

    current_export_path_8_js = os.path.join(current_export_path_js, "Alegere subiect profil Resurse Naturale")
    if( os.path.exists(current_export_path_8_js) == False):
        os.mkdir(current_export_path_8_js)
    current_export_path_8_js = os.path.join(current_export_path_8_js, str(year))
    
    all_students_resurse = filter_all(all_students, profile = "resurse naturale si protectia mediului")

    all_categories = {}
    for i in all_students_resurse:
        all_categories[i.subject3] = "found"
    
    #all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica mi c/c++")
    all_students_biologie = filter_all(all_students_resurse, subject3 = "biologie vegetala si animala")
    all_students_anatomie = filter_all(all_students_resurse, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
    all_students_chimie_organica = filter_all(all_students_resurse, subject3 = "chimie organica teh nivel i/ii")
    all_students_chimie_anorganica = filter_all(all_students_resurse, subject3="chimie anorganica teh nivel i/ii")
    all_students_fizica = filter_all(all_students_resurse, subject3 = "fizica teh")
    

    students_list = [all_students_biologie, all_students_anatomie, all_students_chimie_organica, all_students_chimie_anorganica, all_students_fizica]

    all_grades = []

    for student_type in students_list:
        suma = 0
        for student in student_type:
            suma += student.subject3_grade_final
        suma = float(suma) / float(len(student_type))
        all_grades.append(suma)

    colors = ['#BEEBE9', '#F4DADA', '#ffb6b9', '#f6eec7', '#B28B90']

    
    name_list = ["Biologie", "Anatomie",  "Chimie Organica", "Chimie Anorganica", "Fizica"]
    
    make_barchart_percentage_subject3(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III Profil Resurse Naturale" + str(year)), current_export_path = current_export_path_8, colors = colors)
    make_barchart_percentage_subject3_js(all_students = students_list, all_grades = all_grades, categories_names = name_list, title = ("Procentaj alegere subiectul III Profil Resurse Naturale" + str(year)), current_export_path = current_export_path_8_js, colors = colors)


    #------nota romana mate-info - stiinte ale naturii---------
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

    current_export_path_3_js = os.path.join(current_export_path_js, "Romana mate-info si stiinte")
    if( os.path.exists(current_export_path_3_js) == False):
        os.mkdir(current_export_path_3_js)
    current_export_path_3_js = os.path.join(current_export_path_3_js, str(year))

    grade_mate_info_romana = float(grade_mate_info_romana) / float(len(mate_info))
    grade_stiinte_romana = float(grade_stiinte_romana) / float(len(stiinte))
    grades = [grade_mate_info_romana, grade_stiinte_romana]
    make_barchart_values(grades, ["mate-info", "stiinte"], "Note romana", current_export_path_3, ['#BEEBE9', '#F4DADA'])
    make_barchart_values_js(grades, ["mate-info", "stiinte"], "Note romana", current_export_path_3_js, ['#BEEBE9', '#F4DADA'])
    