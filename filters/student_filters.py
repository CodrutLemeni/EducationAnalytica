
def filter_all(all_students,specialisation = None, grade = None, gender = None, medium = None,
           highschool = None, locality = None, region = None, class_name = None, passed = None):

    all_students = filter_by_specialisation(all_students, specialisation)
    all_students = filter_by_grade(all_students, grade)
    all_students = filter_by_gender(all_students, gender)
    all_students = filter_by_medium(all_students, medium)
    all_students = filter_by_highschool(all_students, highschool)
    all_students = filter_by_locality(all_students, locality)
    all_students = filter_by_region(all_students, region)
    all_students = filter_by_class(all_students, class_name)
    all_students = filter_by_passing(all_students, passed)
    return all_students

def filter_by_specialisation(all_students, specialisation = None):
    '''
        Input:  list of students
                specific specialisation
        Output: list of students with given specialisation
    '''
    if specialisation == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.specialisation == specialisation:
            selected_students.append(current_student)
    return selected_students

def filter_by_grade(all_students, threshold = None):
    '''
        Input: list of Students
        Output: list of Students with grades
                    greather than threshold
    '''
    if threshold == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.final_grade >= threshold:
            selected_students.append(current_student)
    return selected_students

def filter_by_gender(all_students, gender = None):
    '''
        Input:  list of students
                specific gender
        Output: list of students with given gender
    '''
    if gender == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.gender == gender:
            selected_students.append(current_student)
    return selected_students

def filter_by_medium(all_students, medium):
    '''
        Input:  list of students
                specific medium
        Output: list of students with given medium
    '''
    if medium == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.medium == medium:
            selected_students.append(current_student)
    return selected_students

def filter_by_highschool(all_students, highschool = None):
    '''
        Input:  list of students
                specific medium
        Output: list of students with given highschool
    '''
    if highschool == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.highschool.name == highschool:
            selected_students.append(current_student)
    return selected_students

def filter_by_region(all_students, region = None):
    '''
        Input:  list of students
                specific medium
        Output: list of students with given region
    '''
    if region == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.highschool.region == region:
            selected_students.append(current_student)
    return selected_students

def filter_by_locality(all_students, locality = None):
    '''
        Input:  list of students
                specific medium
        Output: list of students with given locality
    '''
    if locality == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.highschool.locality == locality:
            selected_students.append(current_student)
    return selected_students

def filter_by_class(all_students, class_name = None):
    '''
        Input:  list of students
                specific medium
        Output: list of students with given locality
    '''
    if class_name == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.highschool.class_name == class_name:
            selected_students.append(current_student)
    return selected_students

def filter_by_passing(all_students, passed = None):
    if passed == None:
        return all_students

    selected_students = []
    for current_student in all_students:
        if current_student.passed == passed:
            selected_students.append(current_student)
    return selected_students
