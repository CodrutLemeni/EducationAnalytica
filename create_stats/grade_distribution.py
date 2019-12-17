import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import logging
import os

from textwrap import wrap
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_unique_values(df, column):
    """ Get unique values from Pandas DataFrame column.

    Parameters:
        df - Pandas DataFrame object
        column - string, the column name

    Returns:
        list containing the unique values

    """

    return list(df[column].dropna().unique())

def get_all_exam_subjects(df):
    """ Returns a list of all exam subjects present in the dataset.

    Parameters:
        df - Pandas DataFrame object
    
    Returns:
        list of all exam subjects present in the dataset

    """

    return (get_unique_values(df, 'Subiect ea'), get_unique_values(df, 'Subiect eb'), get_unique_values(df, 'Subiect ec'), get_unique_values(df,'Subiect ed'))

def get_exam_category(df, exam):
    """ Return the exam category (ea, eb, ec, ed) based on the name of the subject.

    Params:
        df - Pandas DataFrame object
        exam - string, name of the exam

    Returns:
        label of the corresponding category in the dataset

    Raises:
        AssertionError - if the exam name is not valid

    """

    (ea_exams, eb_exams, ec_exams, ed_exams) = get_all_exam_subjects(df)
    
    if exam in ea_exams:
        return 'Subiect ea'
    elif exam in eb_exams:
        return 'Subiect eb'
    elif exam in ec_exams:
        return 'Subiect ec'
    elif exam in ed_exams:
        return 'Subiect ed'

    raise AssertionError("Exam {} invalid.".format(exam))
    
def grade_label_from_category(category):
    """ Returns the grade label from the category label. (Subiect ea => NOTA_EA)

    Parameters:
        category - string, can be one of (Subiect ea, Subiect eb, Subiect ec, Subiect ed)

    Returns:
        label of grade in the dataset

    """

    return "NOTA_{}".format(category.split(' ')[1].upper())

def plot_grade_distribution(df, subjects, export = None, export_path=""):
    """ Plots the grade distribution based on dataset and given subjects.

    Parameters:
        df - Pandas DataFrame object
        subjects - list of string containing subjects that should be taken into account
                   OR 'all'. In 'all' case all the subjects will be taken into account.
        export - can be one of (None, 'hist'), format in which it will be exported
        export_path - optional, where to export the figure (should end with .png).
                      If not present will save to current directory.
    
    Returns:
        Pandas Series object containing the data used for the plots

    Raises:
        AssertionError - if user provides a subject which is invalid

    """
    
    logging.info("Started export for grade distribution")

    # get all valid exam subjects from dataset via list comprehension
    exam_subjects = [subject for exam_category in get_all_exam_subjects(df)
                    for subject in exam_category]

    data = pd.DataFrame()

    add_vertical_space = False

    if subjects == 'all':
        # all case, text doesn't fit, add some more vertical space
        add_vertical_space = True
        subjects = exam_subjects
    
    for subject in subjects:
        if not subject in exam_subjects:
            raise AssertionError("Subject {} invalid. MUST be one of the following {}".format(subject, exam_subjects))
        
        logging.info("Extracting grades for {}...".format(subject))

        # get category for this subject. e.g 'Subiect ea'
        category = get_exam_category(df, subject)
        
        # add the grates to the dataframe. An example query looks like:
        # df[df['Subiect ea'] == 'Limba romana (REAL)']['NOTA_EA']
        subject_grades = df[df[category] == subject][grade_label_from_category(category)]
        data = pd.concat([data, subject_grades], ignore_index=True)

        logging.info("Successfully extracted {} grades for {}!".format(len(subject_grades), subject))
    
    # filter based on grade
    data = data.where(data > 1)
    
    if export is not None:
        sns.set_context('poster')
        plt.figure(figsize =(16,12))
        
        if export =='hist':
            sns.distplot(data, bins = 100, kde=False,
                         hist_kws = {'edgecolor': 'darkblue', 'linewidth': '1.2'})
        
        plt.xlabel('Grade')
        plt.ylabel('Frequency')

        plt.xticks(np.arange(11))
        # plt.title("\n".join(wrap("Grades Distribution ({})".format(subjects))))
        plt.title("Grades Distribution")

        if add_vertical_space:
            plt.subplots_adjust(top=0.6)

        if export_path:
            plt.savefig(export_path)
            logging.info("Succesfully exported to {}".format(export_path))
        else:
            logging.warning("No export path provided. Figure will be exported in current working directory.")
            plt.savefig('grade_distribution.png')

    return data

if __name__ == "__main__":
    dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    csv_path = os.path.join(dirpath, os.path.join("data","good_bac_2019.csv"))

    export_path = os.path.join(dirpath, os.path.join("plots","bac_2019_grade_distribution.png"))
    
    df = pd.read_csv(csv_path)
    plot_grade_distribution(df, 'all', 'hist', export_path)