import sys
from pathlib import Path
sys.path.append(r'..')
from classes.student import initialize_students
from classes.scholar import initialize_scholars

def read_results(years, type):
    results = {}
    if type == "students":
        results_base_path = r"../data/year/good_bac_year.csv"
    else:
        results_base_path = r"../data/year/good_evn_year.csv"
    for year in years:
        current_results_path = results_base_path.replace("year", year)
        results_csv_file = Path(current_results_path)
        if type == "students":
            results[year] = initialize_students(results_csv_file)
        else:
             results[year] = initialize_scholars(results_csv_file)
    return results

if __name__ == "__main__":
    studs = read_results(['2019'], "scholar")
    print(studs['2019'][5].school)