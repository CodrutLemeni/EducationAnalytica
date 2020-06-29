import sys
import os
import logging
import numpy as np
import json

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
json_export_path = os.path.join(dirpath, r"jsons")

from filters.student_filters import filter_all
from classes.student import initialize_students
from make_line_graph_js import make_line_graph_js

def create_line_graph_js(all_students, current_export_path_js, years):
    
    noStudents = 0

    general_export_path_js = current_export_path_js
#--MEDII----------------------------    

    current_export_path_js = os.path.join(general_export_path_js, "Dupa Medie")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)
    #-----MEDIE ANUALA---------
    
    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in all_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei totale", current_export_path = current_export_path_js, years = years)


    #-----MEDIE PE PROFILE-----

    #-----1.MATE INFO----------

    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students = all_students[year], specialisation="matematica-informatica")

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei la mate-info", current_export_path = current_export_path_js, years = years)

    #-----2.FILO-------------

    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students = all_students[year], specialisation="filologie")

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei la filologie", current_export_path = current_export_path_js, years = years)

    #-----3.STIINTE ALE NATURII-----

    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students = all_students[year], specialisation="stiinte ale naturii")

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei la stiinte ale naturii", current_export_path = current_export_path_js, years = years)

    #-----4.STIINTE SOCIALE-------
    
    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students = all_students[year], specialisation="stiinte sociale")

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei la stiinte ale sociale", current_export_path = current_export_path_js, years = years)

    #-----5.PROFILE TEHNICE/TEHNOLOGICE-----

    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students[year], specialisation_list = ["filologie", "matematica-informatica", "stiinte ale naturii", "stiinte sociale"])

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei la filiera tehnologica si tehnica", current_export_path = current_export_path_js, years = years)

    #----MEDII PE URBAN------

    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students = all_students[year], medium="urban")

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei in zona urbana", current_export_path = current_export_path_js, years = years)

    #-----MEDII PE RURAL----

    crt_students = {}
    for year in years:
        crt_students[year] = filter_all(all_students = all_students[year], medium = "rural")

    all_averages = []
    for year in years:
        average = 0
        noStudents = 0
        for elem in crt_students[year]:
            if elem.final_grade >= 1:
                average += elem.final_grade
                noStudents += 1
        average /= noStudents
        all_averages.append(average)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia mediei in zona rurala", current_export_path = current_export_path_js, years = years)


#-----PROCENTAJE PROMOVABILITATE-----------------
    current_export_path_js = os.path.join(general_export_path_js, "Dupa Procentaj Promovabilitate")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)



    #-----PROCENTAJ PE PROFILE-----

    #-----1.MATE INFO----------

    all_averages = []
    for year in years:
        crt_students = filter_all(all_students = all_students[year], specialisation="matematica-informatica")
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)


    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii la mate-info", current_export_path = current_export_path_js, years = years)

    #-----2.FILO-------------

    all_averages = []
    for year in years:
        crt_students = filter_all(all_students = all_students[year], specialisation="filologie")
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)


    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii la filologie", current_export_path = current_export_path_js, years = years)

    #-----3.STIINTE ALE NATURII-----

    all_averages = []
    for year in years:
        crt_students = filter_all(all_students = all_students[year], specialisation="stiinte ale naturii")
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii la stiinte ale naturii", current_export_path = current_export_path_js, years = years)

    #-----4.STIINTE SOCIALE-------
    
    all_averages = []
    for year in years:
        crt_students = filter_all(all_students = all_students[year], specialisation="stiinte sociale")
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii la stiinte ale sociale", current_export_path = current_export_path_js, years = years)

    #-----5.PROCENTAJ TEHNICE/TEHNOLOGICE-----

    all_averages = []
    for year in years:
        crt_students = filter_all(all_students[year], specialisation_list = ["filologie", "matematica-informatica", "stiinte ale naturii", "stiinte sociale"])
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)


    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii la filiera tehnologica si tehnica", current_export_path = current_export_path_js, years = years)

    #----PROCENTAJ PE URBAN------

    all_averages = []
    for year in years:
        crt_students = filter_all(all_students = all_students[year], medium="urban")
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)


    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii in zona urbana", current_export_path = current_export_path_js, years = years)

    #-----PROCENTAJ PE RURAL----

    all_averages = []
    for year in years:
        crt_students = filter_all(all_students = all_students[year], medium = "rural")
        passed_students = filter_all(all_students=crt_students, passed="Promovat")
        all_averages.append(len(passed_students) / len(crt_students) * 100)

    make_line_graph_js(all_categories = all_averages, OYName = "Medie", title = "Evolutia promovabilitatii in zona rurala", current_export_path = current_export_path_js, years = years)

#--PROCENTAJ ALEGERE SUBIECTUL III
    partial_export_path_js = os.path.join(general_export_path_js, "Dupa Procentaj Alegere SIII")
    if( os.path.exists(partial_export_path_js) == False):
        os.mkdir(partial_export_path_js)
    
    #---1.MATE-INFO--------
    current_export_path_js = os.path.join(partial_export_path_js, "Mate-Info")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)
    
    info = []
    bio = []
    anatomie = []
    chimie_org = []
    chimie_anorg = []
    fizica = []
    for year in years:
        all_students_mate_info = filter_all(all_students[year], specialisation = "matematica-informatica")
        all_students_informatica = filter_all(all_students_mate_info, subject3 = "informatica mi c/c++")
        all_students_biologie = filter_all(all_students_mate_info, subject3 = "biologie vegetala si animala")
        all_students_anatomie = filter_all(all_students_mate_info, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
        all_students_chimie_organica = filter_all(all_students_mate_info, subject3 = "chimie organica teo nivel i/ii")
        all_students_chimie_anorganica = filter_all(all_students_mate_info, subject3 = "chimie anorganica teo nivel i/ii")
        all_students_fizica = filter_all(all_students_mate_info, subject3 = "fizica teo")
        noStudents = len(all_students_mate_info)
        info.append(len(all_students_informatica) / noStudents * 100)
        bio.append(len(all_students_biologie) / noStudents * 100)
        anatomie.append(len(all_students_anatomie) / noStudents * 100)
        chimie_org.append(len(all_students_chimie_organica) / noStudents * 100)
        chimie_anorg.append(len(all_students_chimie_anorganica) / noStudents * 100)
        fizica.append(len(all_students_fizica) / noStudents * 100)
    
    make_line_graph_js(all_categories = info, OYName = "Procent", title = "Procentaj alegere informatica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = bio, OYName = "Procent", title = "Procentaj alegere biologie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = anatomie, OYName = "Procent", title = "Procentaj alegere anatomie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = chimie_org, OYName = "Procent", title = "Procentaj alegere chimie organica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = chimie_anorg, OYName = "Procent", title = "Procentaj alegere chimie anorganica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = fizica, OYName = "Procent", title = "Procentaj alegere fizica", current_export_path = current_export_path_js, years = years)

    #---2.STIINTE ALE NATURII---
    
    current_export_path_js = os.path.join(partial_export_path_js, "Stiinte ale naturii")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)
    
    info = []
    bio = []
    anatomie = []
    chimie_org = []
    chimie_anorg = []
    fizica = []
    for year in years:
        all_students_stiinte= filter_all(all_students[year], specialisation = "stiinte ale naturii")
        all_students_informatica = filter_all(all_students_stiinte, subject3 = "informatica sn c/c++")
        all_students_biologie = filter_all(all_students_stiinte, subject3 = "biologie vegetala si animala")
        all_students_anatomie = filter_all(all_students_stiinte, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
        all_students_chimie_organica = filter_all(all_students_stiinte, subject3 = "chimie organica teo nivel i/ii")
        all_students_chimie_anorganica = filter_all(all_students_stiinte, subject3 = "chimie anorganica teo nivel i/ii")
        all_students_fizica = filter_all(all_students_stiinte, subject3 = "fizica teo")
        noStudents = len(all_students_stiinte)
        info.append(len(all_students_informatica) / noStudents * 100)
        bio.append(len(all_students_biologie) / noStudents * 100)
        anatomie.append(len(all_students_anatomie) / noStudents * 100)
        chimie_org.append(len(all_students_chimie_organica) / noStudents * 100)
        chimie_anorg.append(len(all_students_chimie_anorganica) / noStudents * 100)
        fizica.append(len(all_students_fizica) / noStudents * 100)
    
    make_line_graph_js(all_categories = info, OYName = "Procent", title = "Procentaj alegere informatica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = bio, OYName = "Procent", title = "Procentaj alegere biologie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = anatomie, OYName = "Procent", title = "Procentaj alegere anatomie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = chimie_org, OYName = "Procent", title = "Procentaj alegere chimie organica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = chimie_anorg, OYName = "Procent", title = "Procentaj alegere chimie anorganica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = fizica, OYName = "Procent", title = "Procentaj alegere fizica", current_export_path = current_export_path_js, years = years)


    #---3.FILOLOGIE------

    current_export_path_js = os.path.join(partial_export_path_js, "Filologie")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)
    
    filosoife = []
    logica = []
    sociologie = []
    geo = []
    psiho = []
    economie = []
    for year in years:
        all_students_filologie = filter_all(all_students[year], specialisation = "filologie")
        all_students_filosofie = filter_all(all_students_filologie, subject3 = "filosofie")
        all_students_logica = filter_all(all_students_filologie, subject3 = "logica, argumentare si comunicare")
        all_students_sociologie = filter_all(all_students_filologie, subject3 = "sociologie")
        all_students_geografie = filter_all(all_students_filologie, subject3 = "geografie")
        all_students_psihologie = filter_all(all_students_filologie, subject3 = "psihologie")
        all_students_economie = filter_all(all_students_filologie, subject3="economie")
        noStudents = len(all_students_filologie)
        filosoife.append(len(all_students_filosofie) / noStudents * 100)
        logica.append(len(all_students_logica) / noStudents * 100)
        geo.append(len(all_students_geografie) / noStudents * 100)
        psiho.append(len(all_students_psihologie) / noStudents * 100)
        economie.append(len(all_students_economie) / noStudents * 100)
        sociologie.append(len(all_students_sociologie) / noStudents * 100)
    
    make_line_graph_js(all_categories = filosoife, OYName = "Procent", title = "Procentaj alegere filosofie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = logica, OYName = "Procent", title = "Procentaj alegere logica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = sociologie, OYName = "Procent", title = "Procentaj alegere sociologie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = geo, OYName = "Procent", title = "Procentaj alegere geografie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = psiho, OYName = "Procent", title = "Procentaj alegere psiholohie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = sociologie, OYName = "Procent", title = "Procentaj alegere sociologie", current_export_path = current_export_path_js, years = years)

    #---4.Tehnic-----
    
    current_export_path_js = os.path.join(partial_export_path_js, "Tehnic")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)
    
    bio = []
    anatomie = []
    chimie_org = []
    chimie_anorg = []
    fizica = []
    for year in years:
        all_students_tehnic = filter_all(all_students[year], profile = "tehnic")
        all_students_biologie = filter_all(all_students_tehnic, subject3 = "biologie vegetala si animala")
        all_students_anatomie = filter_all(all_students_tehnic, subject3 = "anatomie si fiziologie umana, genetica si ecologie umana")
        all_students_chimie_organica = filter_all(all_students_tehnic, subject3 = "chimie organica teh nivel i/ii")
        all_students_chimie_anorganica = filter_all(all_students_tehnic, subject3="chimie anorganica teh nivel i/ii")
        all_students_fizica = filter_all(all_students_tehnic, subject3 = "fizica teh")
        noStudents = len(all_students_tehnic)
        bio.append(len(all_students_biologie) / noStudents * 100)
        anatomie.append(len(all_students_anatomie) / noStudents * 100)
        chimie_org.append(len(all_students_chimie_organica) / noStudents * 100)
        chimie_anorg.append(len(all_students_chimie_anorganica) / noStudents * 100)
        fizica.append(len(all_students_fizica) / noStudents * 100)
    
    make_line_graph_js(all_categories = bio, OYName = "Procent", title = "Procentaj alegere biologie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = anatomie, OYName = "Procent", title = "Procentaj alegere anatomie", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = chimie_org, OYName = "Procent", title = "Procentaj alegere chimie organica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = chimie_anorg, OYName = "Procent", title = "Procentaj alegere chimie anorganica", current_export_path = current_export_path_js, years = years)
    make_line_graph_js(all_categories = fizica, OYName = "Procent", title = "Procentaj alegere fizica", current_export_path = current_export_path_js, years = years)



if __name__== "__main__":
    base_path = os.path.join(dirpath, r"data")
    all_students = {}
    years = [2015, 2016, 2017, 2019]
    for year in years:
        csv_path = os.path.join(base_path, "good_bac_"+str(year)+".csv" )
        all_students[year] = initialize_students(csv_path)
    current_export_path_js = os.path.join(json_export_path, "Line Graphs")
    if( os.path.exists(current_export_path_js) == False):
        os.mkdir(current_export_path_js)
    
    create_line_graph_js(all_students = all_students, current_export_path_js = current_export_path_js, years = years)