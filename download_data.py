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

    


