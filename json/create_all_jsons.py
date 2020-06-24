import sys
import os
import logging
import numpy as np
import json

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
json_export_path = os.path.join(dirpath, r"jsons")

from filters.student_filters import filter_all
from make_barchart_js import make_barchart_percentage_js
from make_barchart_js import make_barchart_values_js
from make_barchart_js import make_barchart_percentage_subject3_js
from classes.student import initialize_students
from create_barchart_js import create_barchart_percentage_js
from create_distribution_json import create_distribution_json

if __name__ == "__main__" :
    base_path = os.path.join(dirpath, r"data")
    for year in range(2015,2020):
        try:
            csv_path = os.path.join(base_path, "good_bac_"+str(year)+".csv" )
            all_students = initialize_students(csv_path)
            current_export_path_js = os.path.join(json_export_path, "Horizontal Bar Charts")
            if( os.path.exists(current_export_path_js) == False):
                os.mkdir(current_export_path_js)
            create_barchart_percentage_js(all_students = all_students, current_export_path_js = current_export_path_js, year = year)


            create_distribution_json(all_students, year)

        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            print(f"Year {year} went wrong")    