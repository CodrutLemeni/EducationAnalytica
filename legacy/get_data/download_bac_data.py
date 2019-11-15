import re
import requests
from bs4 import BeautifulSoup
import os

output_file = r"D:\Work\bac_stats\stats_bac\data\raw_data.txt"

def get_data_website(page_url):

    url = base_url.format(1)
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')

    txt = ';LuatDePe_BacalaureatEduRo\["[a-z,A-Z,<,>, ,.,-]*?\"]="[0-9,.]+?";'
    x = re.findall(txt, content)
    f = open(output_file, "a")
    f.write(str(x)+'\n')
    f.close()


if __name__ == "__main__":

    if os.path.exists( output_file ):
        os.remove( output_file )

    base_url = "http://static.bacalaureat.edu.ro/2018/rapoarte/rezultate/dupa_medie/page_"

    for idx in range(1, 9668 ):
        new_url = base_url + str(idx) + '.html'
        get_data_website(new_url)