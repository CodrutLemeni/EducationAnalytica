from get_genders import get_boys_and_girls
import os
import msvcrt as m
import sys

unlabelled_names = get_boys_and_girls()

girls_file = open(r'D:\Work\bac_stats\stats_bac\all_data\girls_names_codrut.txt','a')
boys_file = open(r'D:\Work\bac_stats\stats_bac\all_data\boys_names_codrut.txt','a')

for name in unlabelled_names:
    print(name)
    key = sys.stdin.read(1)
    if key == 'g':
        print('girl')
        girls_file.write('\n'+name[0])
    elif key == 'b':
        print('boy')
        boys_file.write('\n'+name[0])
    elif key == 'n':
        continue
    else:
        girls_file.close()
        boys_file.close()
        break
