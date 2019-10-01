import operator


def make_dict( input_file ):
    fin = open( input_file, 'r' )
    data = fin.read()
    data = data.split('\n')

    name_dictionary = {}
    for name in data:
        name_dictionary[ name.upper() ] = 1 
    fin.close()
    return name_dictionary

def get_boys_and_girls():

    boys_dictionary = make_dict("boys_names_codrut.txt")
    girls_dictionary = make_dict("girls_names_codrut.txt")

    fin = open('mate_info.txt','r')
    results_data = fin.read()
    results_data = results_data.split('\n')

    no_boys = 0
    no_girls = 0
    no_bad = 0

    dict_unlabeled_names = {}

    boys_grades = {}
    girls_grades = {}

    for name in results_data:
        name_list = name.split(' ')
        name_list.pop(-1)
        name_list.pop(0)
        name_list.pop(0)

        all_names = []
        for first_name in name_list:
            names = first_name.split('-')
            for cr_name in names:
                all_names.append( cr_name)

        is_boy = is_girl = is_bad = 0 
        for first_name in all_names:
            if len( first_name ) <= 2:
                continue
            if '.' in first_name:
                continue

            first_name = first_name.split('-')[0]
            if first_name in boys_dictionary :
                is_boy = 1
            elif first_name in girls_dictionary:
                is_girl = 1
            else:
                is_bad = 1
                if first_name in dict_unlabeled_names :
                    dict_unlabeled_names [ first_name ] += 1
                else:
                    dict_unlabeled_names [ first_name ] = 1
        if is_boy == is_girl and is_boy == 1:
            # print( all_names )  
            pass
        elif is_boy == is_girl and is_boy == 0:
            # print( all_names )  
            pass
                
        else:
            grade = name.split(' ')[-1]
            grade = float(grade)

            if is_boy == 1:
                if grade in boys_grades:
                    boys_grades [ grade ] += 1
                else:
                    boys_grades [ grade ] = 1
            else:
                if grade in girls_grades:
                    girls_grades [ grade ] += 1
                else:
                    girls_grades [ grade ] = 1

            no_boys += is_boy
            no_girls += is_girl
            no_bad += is_bad

    boys_grades_file = open('final_grades_boys.txt','w')
    girls_grades_file = open('final_grades_girls.txt','w')

    boys_grades = sorted(boys_grades.items(), key=operator.itemgetter(0) , reverse = True)
    girls_grades = sorted(girls_grades.items(), key=operator.itemgetter(0) , reverse = True)



    for grade in boys_grades:
        boys_grades_file.write(str(grade[0]) + ' ' + str(grade[1]) + '\n' )

    for grade in girls_grades:
        girls_grades_file.write(str(grade[0]) + ' ' + str(grade[1]) + '\n' )

    
    sorted_x = sorted(dict_unlabeled_names.items(), key=operator.itemgetter(1) , reverse = True)


    # print(sorted_x)   
    print( "Number Boys: {1}",no_boys)
    print( "Number Girls: {1}",no_girls)
    print(no_bad)
    
    return sorted_x


get_boys_and_girls()

