import operator

input_file = r'D:\Work\bac_stats\stats_bac\all_data\parsed_data.txt'
output_file = r'D:\Work\bac_stats\stats_bac\all_data\gender_results.txt'


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

    boys_dictionary = make_dict(r"D:\Work\bac_stats\stats_bac\all_data\boys_names_codrut.txt")
    girls_dictionary = make_dict(r"D:\Work\bac_stats\stats_bac\all_data\girls_names_codrut.txt")

    fin = open(input_file,'r')
    results_data = fin.read()
    results_data = results_data.split('\n')

    out = open(output_file,'w')

    no_boys = 0
    no_girls = 0
    no_bad = 0

    dict_unlabeled_names = {}

    for name in results_data:
        name_list = name.split(' ')
        if len(name_list) < 3:
            pass
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
                out.write('M '+ str(grade)+'\n')
            else:
                out.write('F '+ str(grade)+'\n')


            no_boys += is_boy
            no_girls += is_girl
            no_bad += is_bad


    sorted_x = sorted(dict_unlabeled_names.items(), key=operator.itemgetter(1) , reverse = True)


    # print(sorted_x)   
    print("Number Boys: {1}",no_boys)
    print("Number Girls: {1}",no_girls)
    print("Number Unknown: {1}",no_bad)

    
    return sorted_x


if __name__ == "__main__":
    get_boys_and_girls()