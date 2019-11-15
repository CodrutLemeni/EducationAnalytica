import os
import sys

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ) 

from classes.student import initialize_students



if __name__ == "__main__":
    csv_path = os.path.join(dirpath, r"data")
    csv_path = os.path.join(csv_path, r"good_bac_2019.csv")

    all_students = initialize_students(csv_path)
    print(all_students)
