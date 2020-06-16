import sys
from os import path
import os.path
from pathlib import Path
import glob

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

from classes.student import *
from classes.highschool import *
from filters.student_filters import filter_all
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
import json
#in what quantile are you with the grade you have, depending on the profile

input_csv_students = Path("../data")
input_csv_units = Path("../unitati_scolare_2019.csv")

json_export_path = os.path.join(dirpath, r"jsons")
mapcharts_path = os.path.join(json_export_path, "Mapcharts")

def create_map_json(filename_students, current_export_path):
    final_dict = {
        "meta": {
            "type": "MAP_CHART",
            "title": "Media pe judete",
            },
        "series": []
    }
    temp_dict = {} # stores the mean and number of students for each county
    all_students = initialize_students(filename_students, input_csv_units)
    count_noregion = 0
    for current_student in all_students:
        if current_student.highschool.region not in temp_dict:
            county = current_student.highschool.region
            student_countyx = filter_all(all_students, region=county)
            grades = returngrades(student_countyx)
            mean = sum(grades) / len(grades)
            number = len(grades)
            temp_dict[str(county)] = (mean, number)
        if (current_student.highschool.name=="?"):
            count_noregion=count_noregion+1
    #the code of the institution cannot be found
    print(count_noregion)
    # temp_dict = OrderedDict(sorted(temp_dict.items()))

    for (k,v) in temp_dict.items():
        new_dict = {}
        new_dict["key"] = k
        new_dict["value"] = v[0]
        extra_1 = {
            "label": "Nr. elevi",
            "value": v[1]
        }
        extra_2 = {
            "label": "Media",
            "value": v[0]
        }
        extra = [extra_1, extra_2]
        new_dict["extra"] = extra
        final_dict["series"].append(new_dict)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(final_dict)
    f.write(jsonDict)


if __name__== "__main__":
    base_path = os.path.join(dirpath, r"data")
    for year in range(2015,2020):
        try:
            csv_path = os.path.join(base_path, "good_bac_"+str(year)+".csv" )
            current_export_path_js = os.path.join(mapcharts_path, "mapchart " + str(year))
            create_map_json(csv_path, current_export_path_js)
            # exit()
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            print(f"Year {year} went wrong")
