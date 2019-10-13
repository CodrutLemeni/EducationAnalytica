import csv
results_csv_file = r'/home/sebastian/Dropbox/Facultate/BacStats/good_bac_2019.csv'
def get_third_subjects():
    subjects = set()
    with open(results_csv_file) as file:
        csv_readear = csv.reader(file, delimiter=',')
        for row in csv_readear:
            subjects.add(row[14].lower())
    
    file = open('subjects.txt', 'w')
    for subject in subjects:
        file.write(subject + '\n')
    file.close()


if __name__ == "__main__":
    get_third_subjects()

