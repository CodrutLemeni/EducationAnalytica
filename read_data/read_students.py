import csv
import sys
from pathlib import Path
sys.path.append(r'..')
from classes.student import *
def read_results(years):
    results = {}
    results_base_path = r"../data/year/good_bac_year.csv"
    schools_csv_file = Path(r"../data/2019/unitati_scolare_2019.csv")
    for year in years:
        current_results_path = results_base_path.replace("year", year)
        results_csv_file = Path(current_results_path)
        results[year] = initialize_students(results_csv_file, schools_csv_file)
    return results


    

