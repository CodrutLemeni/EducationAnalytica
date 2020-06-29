import sys
import os
import logging
import numpy as np
import json

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.student import initialize_students
from filters.student_filters import filter_all


def create_distribution_json(students, year=None):
    plots_path = os.path.join(dirpath, r"jsons")
    distrib_path = os.path.join(plots_path, r"Distributions")

    if os.path.exists(distrib_path) == False:
        os.mkdir(distrib_path)

    make_distribution_json(students, year, "Toate Specializarile", distrib_path)

    for cr_spec in ["matematica-informatica", "filologie", "stiinte ale naturii"]:
        cr_students = filter_all(students, specialisation=cr_spec)
        make_distribution_json(students, year, cr_spec, distrib_path)


def make_distribution_json(students, year=None, specialization=None, export_folder=None):
    title = "Grade Distribution {} - {}".format(specialization, year)
    export_file = os.path.join(export_folder, title)

    final_dict = {}
    final_dict["meta"] = {
        "type": "GRADE_DIST",
        "title": title,
        "year": year,
        "xAxisName": "Grades",
        "yAxisName": "Frequency"
    }

    grades_dict = {}

    for cr_stud in students:
        if cr_stud.subject1_grade_final not in grades_dict.keys():
            grades_dict[cr_stud.subject1_grade_final] = 0
        if cr_stud.subject2_grade_final not in grades_dict.keys():
            grades_dict[cr_stud.subject2_grade_final] = 0
        if cr_stud.subject3_grade_final not in grades_dict.keys():
            grades_dict[cr_stud.subject3_grade_final] = 0

        grades_dict[cr_stud.subject1_grade_final] += 1
        grades_dict[cr_stud.subject2_grade_final] += 1
        grades_dict[cr_stud.subject3_grade_final] += 1

    series_array = []
    for key, value in grades_dict.items():
        temp_dict = {}
        temp_dict["key"] = key
        temp_dict["value"] = value
        series_array.append(temp_dict)

    final_dict["series"] = series_array
    file = open(export_file, "w")
    file.write(json.dumps(final_dict))


if __name__ == "__main__":
    base_path = os.path.join(dirpath, r"data")
    for year in range(2015, 2020):
        try:
            csv_path = os.path.join(base_path, "good_bac_" + str(year) + ".csv")
            cr_students = initialize_students(csv_path)
            create_distribution_json(cr_students, year)
            exit()
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            print(f"Year {year} went wrong")
