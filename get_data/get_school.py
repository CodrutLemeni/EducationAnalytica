import re
import urllib.request
import os
import requests
from bs4 import BeautifulSoup

output_file = r"/home/cosmi/BAC/BAC_2019_statistics/data/raw_county.txt"

def get_data_website(page_url, idx):

    # opener = urllib.request.FancyURLopener({})
    # f = opener.open(page_url)
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    f = soup.prettify()
    txt = '(<a href="......*.lista_unitati.index.html">.*\n)(.*)(\n.*)'
    x = re.findall(txt, f)
    f = open(output_file, "a")
    for s in x:
        string = s[1]
        f.write(string+'\n')
    f.close()


if __name__ == "__main__":

    if os.path.exists( output_file ):
        os.remove( output_file )

    base_url = "http://static.bacalaureat.edu.ro/2018/rapoarte/rezultate/dupa_medie/page_"

    for idx in range(1, 9668 ):
        new_url = base_url + str(idx) + '.html'
        get_data_website(new_url, idx)