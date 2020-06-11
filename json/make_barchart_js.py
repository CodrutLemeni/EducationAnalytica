import numpy as np
import matplotlib.pyplot as plt
import json

def make_barchart_percentage_js(all_categories, all_categories_good, categories_names, title, current_export_path):

    percentage = []
    for i in range(len(all_categories)):
        percentage.append(float(len(all_categories_good[i])) / float(len(all_categories[i])) * 100)

    meta = {}
    dataDict = {}
    dataDict["series"] = []
    
    
    meta["type"] = "HORIZONTAL_BAR_CHART"
    meta["title"] = title
    meta["xAxisName"] = "Procentaj"
    dataDict["meta"] = meta
    for i in range(len(all_categories)):
        label = {}
        crtElem = {}
        crtElem["extra"] = []

        crtElem["key"] = categories_names[i]
        crtElem["value"] = percentage[i]
        label["label"] = "Nr. elevi promovati"
        label["value"] = len(all_categories_good[i])
        crtElem["extra"].append(label)
        dataDict["series"].append(crtElem)

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

def make_barchart_values_js(all_categories, categories_names, title, current_export_path):
    meta = {}
    dataDict = {}
    dataDict["series"] = []
    
    
    meta["type"] = "HORIZONTAL_BAR_CHART"
    meta["title"] = title
    meta["xAxisName"] = "Nota"
    dataDict["meta"] = meta
    for i in range(len(all_categories)):
        crtElem = {}
        crtElem["extra"] = []

        crtElem["key"] = categories_names[i]
        crtElem["value"] = all_categories[i]
        dataDict["series"].append(crtElem)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(dataDict)
    f.write(jsonDict)