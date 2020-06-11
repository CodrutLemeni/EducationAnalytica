import sys
import logging
from pathlib import Path
import csv
import os
import numpy

class Section:
    def __init__(self, county, total_voters, present_voters, men_18_24, women_18_24, total_18_24 = 0):
        self.county = county
        self.total_voters = total_voters
        self.present_voters = present_voters
        self.men_18_24 = int(men_18_24)
        self.women_18_24 = int(women_18_24)
        self.total_18_24 = int(men_18_24) + int(women_18_24)


    

def read_sections(csv_file):
    with open(csv_file, encoding='utf8') as file:
        reader = csv.reader(file)
        sections = []
        line = 0
        for row in reader:
            if line == 0:
                line += 1
                continue
            current_section = Section(row[0], row[7], row[12], row[13], row[18])
            sections.append(current_section)
            
    return sections

def get_attendance_counties():
    csv_file = os.path.abspath(os.path.join(os.getcwd(), "Data/presence_president_2019.csv"))
    sections = read_sections(csv_file)
    total_counties = {}
    present_counties = {}
    i = 0
    for section in sections:
        i += 1
        if (i == 1) or (section.county == 'SR'):
            continue
        if section.county in total_counties.keys():
            total_counties[section.county] += int(section.present_voters)
            present_counties[section.county] += int(section.total_18_24)
        else:
            total_counties[section.county] = int(section.present_voters)
            present_counties[section.county] = int(section.total_18_24)
    percentage_counties = {}
   
    
    for key in total_counties.keys():
        percentage_counties[key] = (present_counties[key] / total_counties[key])
        i += 1
    return percentage_counties
    


if __name__ == "__main__":

    all_counties_percentage = get_attendance_counties()
    print(all_counties_percentage)
    