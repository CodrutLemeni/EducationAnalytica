import numpy as np
import matplotlib.pyplot as plt
import json

def make_barchart_percentage_js(all_categories, all_categories_good, categories_general_names, categories_particular_names, title, current_export_path):

    meta = {}
    dataDict = {}
    dataDict["series_list"] = []
    
    
    meta["type"] = "HORIZONTAL_BAR_CHART_GROUPED"
    meta["title"] = title
    meta["xAxisName"] = "Procentaj"
    dataDict["meta"] = meta
    
    for i in range(len(categories_general_names)):
        crt_series_with_name = {}
        crt_series = []
        crt_series_with_name["name"] = categories_general_names[i]
        crt_list = all_categories[i]
        crt_list_passed = all_categories_good[i]
        for j in range(len(all_categories[i])):
            label = {}
            crt_elem = {}
            crt_elem["extra"] = []

            crt_elem["key"] = categories_particular_names[j]
            crt_elem["value"] = crt_list_passed[j] / crt_list[j] * 100
            label["label"] = "Nr. elevi promovati"
            label["value"] = crt_list[j]
            crt_elem["extra"].append(label)
            crt_series.append(crt_elem)
        crt_series_with_name["series"] = crt_series
        dataDict["series_list"].append(crt_series_with_name)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(dataDict)
    f.write(jsonDict)

def make_barchart_percentage_subject3_js(all_students, all_grades, categories_names, title, current_export_path):

    total_students = 0
    for students in all_students:
        total_students += len(students)

    percentage = []

    for i in range(len(all_students)):
        percentage.append(float(len(all_students[i])) / float(total_students) * 100)

    meta = {}
    dataDict = {}
    dataDict["series"] = []
    
    
    meta["type"] = "HORIZONTAL_BAR_CHART"
    meta["title"] = title
    meta["xAxisName"] = "Procentaj"
    dataDict["meta"] = meta
    for i in range(len(categories_names)):
        label = {}
        crtElem = {}
        crtElem["extra"] = []

        crtElem["key"] = categories_names[i]
        crtElem["value"] = percentage[i]
        label["label"] = "Nr. elevi care au ales acest subiect"
        label["value"] = len(all_students[i])
        crtElem["extra"].append(label)
        label2 = {}
        label2["label"] = "Media la acest subiect"
        label2["value"] = round(all_grades[i], 2)
        crtElem["extra"].append(label2)
        dataDict["series"].append(crtElem)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(dataDict)
    f.write(jsonDict)

def make_barchart_values_js(all_categories, categories_general_names, categories_particular_names, title, current_export_path):

    meta = {}
    dataDict = {}
    dataDict["series_list"] = []
    
    
    meta["type"] = "HORIZONTAL_BAR_CHART_GROUPED"
    meta["title"] = title
    meta["xAxisName"] = "Nota"
    dataDict["meta"] = meta
    
    for i in range(len(categories_general_names)):
        crt_series_with_name = {}
        crt_series = []
        crt_series_with_name["name"] = categories_general_names[i]
        crt_list = all_categories[i]
        for j in range(len(all_categories[i])):
            label = {}
            crt_elem = {}
            crt_elem["extra"] = []

            crt_elem["key"] = categories_particular_names[j]
            crt_elem["value"] = crt_list[j]

            crt_series.append(crt_elem)
        crt_series_with_name["series"] = crt_series
        dataDict["series_list"].append(crt_series_with_name)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(dataDict)
    f.write(jsonDict)


def make_stacked_barchart_js(all_categories, vertical_names, horizontal_names, title, current_export_path):
    meta = {}
    dataDict = {}
    dataDict["series_list"] = []
    
    
    meta["type"] = "HORIZONTAL_BAR_CHART_STACKED"
    meta["title"] = title
    meta["xAxisName"] = "Procentaj"
    dataDict["meta"] = meta
    
    for i in range(len(horizontal_names)):
        crt_series_with_name = {}
        crt_series = []
        crt_series_with_name["name"] = horizontal_names[i]
        
        for j in range(len(all_categories)):
            crt_list = all_categories[j]
            label = {}
            crt_elem = {}
            crt_elem["extra"] = []

            crt_elem["key"] = vertical_names[j]
            crt_elem["value"] = crt_list[i] / sum(crt_list) * 100
            label["label"] = "Numar elevi"
            label["value"] = crt_list[i]
            crt_elem["extra"].append(label)
            crt_series.append(crt_elem)
        crt_series_with_name["series"] = crt_series
        dataDict["series_list"].append(crt_series_with_name)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(dataDict)
    f.write(jsonDict)