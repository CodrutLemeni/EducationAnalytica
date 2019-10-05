import requests
import time
import logging
import pandas as pd
from bs4 import BeautifulSoup

def get_pages_number(base_url):
    """ Returns pages number from first page derived from base URL.

    Raises:
        Exception - if request fails for any reason (status_code != 200)

    """
    url = base_url.format(1)
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed Request. Aborting..")

    soup = BeautifulSoup(response.text, 'html.parser')
    last_page_number = int(soup.findAll('option', class_="opte")[1].getText().split(' ')[1])

    return last_page_number

def export_csv(parsed_records):
    # convert to dataframe and save in .csv
    df = pd.DataFrame(parsed_records, columns=['high_school', 'romanian_grade', 'county',
                'specialisation', 'profile_exam_name', 'profile_exam_grade',
                'optional_exam_name', 'optional_exam_grade', 'passed'])

    df.to_csv('results.csv', index=None)

# initialise logger, url of data, and compute number of pages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
base_url = 'http://static.bacalaureat.edu.ro/2018/rapoarte/rezultate/dupa_medie/page_{}.html'
parsed_records = []
pagesNumber = get_pages_number(base_url)

for idx in range(1, pagesNumber + 1):
    url = base_url.format(idx)

    logging.info('Making GET request to {}'.format(url))

    response = requests.get(url)

    logging.info('Received Response {}'.format(response.status_code))

    if response.status_code == 200:
        logging.info("Saving Records from page {}".format(idx))
        soup = BeautifulSoup(response.text, 'html.parser')

        # filter table rows to only get relevant student data
        records = []

        for row in soup.findAll('tr'):
            row_class = row.get('class')
            if row_class != None and row_class[0] in ['tr1', 'tr2']:
                records.append(row)

        for record_idx in range(0, len(records), 2):
            # for each student there are 2 rows in the table, this
            # is why we have 2 data objects for each record
            record_row1 = records[record_idx]
            record_row2 = records[record_idx + 1]

            data_row1 = record_row1.find_all('td')
            data_row2 = record_row2.find_all('td')

            # get general info
            high_school = data_row1[2].getText()
            county = data_row1[3].getText()
            specialisation = data_row1[6].getText()

            # get profile exam and optional exam names
            profile_exam_name = data_row1[14].getText()
            optional_exam_name = data_row1[15].getText()

            # get grades and passed/failed status
            romanian_grade = float(data_row1[10].getText())
            profile_exam_grade = float(data_row2[6].getText())
            optional_exam_grade = float(data_row2[9].getText())

            passed = True if 'REUSIT' in record_row1.find('script').getText() else False

            parsed_records.append([high_school, romanian_grade, county, specialisation, profile_exam_name,
                    profile_exam_grade, optional_exam_name, optional_exam_grade, passed])

    # checkpoint, save progress every 100 pages
    if idx % 100 == 0:
        logging.info("Checkpoint on page {}. Saving...".format(idx))
        export_csv(parsed_records)

    # sleep so we won't get timed out
    # time.sleep(0.1)

# if done, save final(full) version
export_csv(parsed_records)
