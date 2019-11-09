from read_data.read_students import read_results
from create_stats.create_linegraphs import make_gender_linegraph
if __name__ == "__main__":
    years = ['2019']
    all_students = read_results(years)
    make_gender_linegraph(all_students, years)