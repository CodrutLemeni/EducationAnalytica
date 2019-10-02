
from selenium import webdriver
import re
import urllib.request

def get_data_website(page_url):
    # driver = webdriver.Chrome(executable_path=r'C:\Users\Codru\node_modules\chromedriver\lib\chromedriver\chromedriver.exe') 

    # driver.get(page_url)
    # content = driver.page_source
    # driver.close()
    opener = urllib.request.FancyURLopener({})
    f = opener.open(page_url)
    content = f.read()
    content = content.decode("utf-8")

    txt = ';LuatDePe_BacalaureatEduRo\["[a-z,A-Z,<,>, ,.,-]*?\"]="[0-9,.]+?";'
    x = re.findall(txt, content)
    f = open("raw_data.txt", "a")
    f.write(str(x))
    f.close()


if __name__ == "__main__":
    
    base_url = "http://static.bacalaureat.edu.ro/2019/rapoarte/rezultate/dupa_medie/page_"

    for idx in range(1, 9668 ):
        new_url = base_url + str(idx) + '.html'
        get_data_website ( new_url )