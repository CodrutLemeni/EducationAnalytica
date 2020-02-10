import sys
import os
from pathlib import Path

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

from classes.student import initialize_students


results_base_path = os.path.join(dirpath,"data")
results_base_path = os.path.join(results_base_path,"good_bac_year.csv")


def read_results(years):
    results = {}
    # results_base_path = r"../data/good_bac_year.csv"
    # schools_csv_file = Path(r"../data/unitati_scolare_2019.csv")
    for year in years:
        current_results_path = results_base_path.replace("year", year)
        results_csv_file = Path(current_results_path)
        # results[year] = initialize_students(results_csv_file, schools_csv_file)
        results[year] = initialize_students(results_csv_file)
    return results
