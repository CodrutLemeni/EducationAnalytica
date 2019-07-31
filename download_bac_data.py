<<<<<<< HEAD
from selenium import webdriver
import re

def get_data_website(page_url):
    driver = webdriver.Chrome(executable_path=r'C:\Users\Codru\node_modules\chromedriver\lib\chromedriver\chromedriver.exe') 

    driver.get(page_url)
    content = driver.page_source
    driver.close()

    txt = ';LuatDePe_BacalaureatEduRo\["[a-z,A-Z,<,>, ,.,-]*?\"]="[0-9,.]+?";'
    x = re.findall(txt, content)
    f = open("data.txt", "a")
    f.write(str(x))
    f.close()

base_url = "http://static.bacalaureat.edu.ro/2019/rapoarte/rezultate/dupa_medie/page_"

for idx in range( 9668 ):
    new_url = base_url + str(idx) + '.html'
    get_data_website ( new_url )
=======
import urllib.request
import array
import re

male_names = {"\0"}
female_names = {"\0"}
    
#page iterations
#for i in range(1, 13610):
i=1
opener = urllib.request.FancyURLopener({})
url = "http://static.bacalaureat.edu.ro/2019/rapoarte/rezultate/dupa_medie/page_{}.html"
f = opener.open(url.format(i))
content = f.read()

#convert file from binary to char
html = content.decode("utf-8")

splitted_text = re.split("REUSIT", html)
#for j in range (0, len(splitted_text) - 1):
#split_for_name = re.split("LuatDePeBacalaureatEduRo\[]=\"", splitted_text);

    


>>>>>>> 862ae6f41d71d3b260aaa175f667edb5594316ec
