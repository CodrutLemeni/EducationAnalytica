import re
import urllib.request

#function for the students that passed the examn
def get_specializations_for_graduates(url):
    #list initialization
    specialization_list = []

    #open and read the url
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    html = content.decode("utf-8")

    #split the text for each student
    splitted_text = re.split("REUSIT", html)

    #search the specialization for each student
    for i in range(1,11):
        mate_info = re.search("MATEMATICA-.*INFORMATICA", splitted_text[i])

        tehnician = re.search("TEHNICIAN.*", splitted_text[i])

        st_sociale = re.search("STIINTE.*SOCIALE", splitted_text[i])
        st_ale_naturii = re.search("STIINTE ALE NATURII", splitted_text[i])

        filologie = re.search("FILOLOGIE", splitted_text[i])

        muzica = re.search("MUZICA", splitted_text[i])

        sportiv = re.search("LICEU CU.*PROGRAM.*SPORTIV", splitted_text[i])

        pedagogie = re.search("INVATATOR -.*EDUCATOARE", splitted_text[i])

        if (mate_info):
            specialization_list.append("MATEMATICA INFORMATICA")
        elif (tehnician):
            specialization_list.append("TEHNICIAN")
        elif (st_sociale):
            specialization_list.append("STIINTE SOCIALE")
        elif (st_ale_naturii):
            specialization_list.append("STIINTE ALE NATURII")
        elif (filologie):
            specialization_list.append("FILOLOGIE")
        elif (muzica):
            specialization_list.append("MUZICA")
        elif (sportiv):
            specialization_list.append("LICEU CU PROGRAM SPORTIV")
        elif (pedagogie):
            specialization_list.append("INVATATOR - EDUCATOARE")
        else:
            specialization_list.append("ALTA SPECIALIZARE")
    return specialization_list


# #function for the students that failled the examn
# def get_specializations_for_failing(url):
#     #list initialization
#     specialization_list = []

#     #open and read the url
#     opener = urllib.request.FancyURLopener({})
#     f = opener.open(url)
#     content = f.read()
#     html = content.decode("utf-8")

#     #split the text for each student
#     splitted_text = re.split("RESPINS", html)

#     #search the specialization for each student
#     for i in range(1,11):
#         mate_info = re.search("MATEMATICA-.*INFORMATICA", splitted_text[i])

#         tehnician = re.search("TEHNICIAN.*", splitted_text[i])

#         st_sociale = re.search("STIINTE.*SOCIALE", splitted_text[i])
#         st_ale_naturii = re.search("STIINTE ALE NATURII", splitted_text[i])

#         filologie = re.search("FILOLOGIE", splitted_text[i])

#         muzica = re.search("MUZICA", splitted_text[i])

#         sportiv = re.search("LICEU CU.*PROGRAM.*SPORTIV", splitted_text[i])

#         pedagogie = re.search("INVATATOR -.*EDUCATOARE", splitted_text[i])

#         if (mate_info):
#             specialization_list.append("MATEMATICA INFORMATICA")
#         elif (tehnician):
#             specialization_list.append("TEHNICIAN")
#         elif (st_sociale):
#             specialization_list.append("STIINTE SOCIALE")
#         elif (st_ale_naturii):
#             specialization_list.append("STIINTE ALE NATURII")
#         elif (filologie):
#             specialization_list.append("FILOLOGIE")
#         elif (muzica):
#             specialization_list.append("MUZICA")
#         elif (sportiv):
#             specialization_list.append("LICEU CU PROGRAM SPORTIV")
#         elif (pedagogie):
#             specialization_list.append("INVATATOR - EDUCATOARE")
#         else:
#             specialization_list.append("ALTA SPECIALIZARE")

#     return specialization_list

#pages with passing students
for i in range (1, 8922):
    opener = urllib.request.FancyURLopener({})
    url = "http://static.bacalaureat.edu.ro/2019/rapoarte/rezultate/dupa_medie/page_{}.html"
    specialization_list = get_specializations_for_graduates(url.format(i))
    file = open("specialization_list.txt", "a")
    for specialization in specialization_list:
        file.write(specialization + "\n")
    file.close()

#pages with failling students
# for i in range (8922, 13610):
#     opener = urllib.request.FancyURLopener({})
#     url = "http://static.bacalaureat.edu.ro/2019/rapoarte/rezultate/dupa_medie/page_{}.html"
#     specialization_list = get_specializations_for_failing(url.format(i))
#     result_name = "specialization_list_page_{}.txt"
#     file = open(result_name.format(i), "w")
#     for specialization in specialization_list:
#         file.write(specialization + "\n")
#     file.close()

    