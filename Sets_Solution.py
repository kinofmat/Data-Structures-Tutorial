"""
Written by Kai Matkin

This is a SOLUTION. Review over this code only after you have tried to
solve the problems on your own. 

This code takes grades from three different sections of a course and performs 
various calculations to interpret the data.
"""

"""This will simply return the number of all of the grades from the sections 
combined. This can be used to infer the number of students in the course."""
def combine_sections_size(data1, data2, data3):
    course_size = len(data1) + len(data2) + len(data3)
    return course_size
    

"""Implement code to this function so that it will count the number of unique 
grades from the section that is passed to it"""
def unique_grades(data):
    # Does this look a little familiar? I used the same principle in the next 
    # function, but repeated 3 times for each class section.
    setion = set()
    for grade in data:
        setion.add(grade)
    return len(setion) #This part needs to return the length of the set. 

"""
Part of this code is already implemented for you. Modify the function so that
it will combine the three sets into one set."""
def course_set(data1, data2, data3):
    set1 = set()
    for grade in data1:
        set1.add(grade)
    set2 = set()
    for grade in data2:
        set2.add(grade)
    set3 = set()
    for grade in data3:
        set3.add(grade)
    # I used the shorthand for unions, you could also use the longhand version
    unique_set = set1 | set2 | set3  
    return unique_set

"""Design code for this function to utilize sets in searching for a grade within 
the combined grades from all sections."""
def search_grades(data1, data2, data3, find):
    # Since the previous function already combined all of the sets we just needed
    # to assign it to a local variable and then check for set membership here.
    if find in course_set(data1, data2, data3):
        return True
    else:
        return False

"""Part of this function is already implemented for you. Modify the code to 
utilize sets in finding the common grades between each section"""
def common_grades(data1, data2, data3):
    set1 = set()
    for grade in data1:
        set1.add(grade)
    set2 = set()
    for grade in data2:
        set2.add(grade)
    set3 = set()
    for grade in data3:
        set3.add(grade)
    # I used the shorthand for intersects, you could also use the longhand version
    common_set = set1 & set2 & set3
    return common_set


section01 = [100, 76, 0, 80, 94, 93, 65, 100, 75, 95, 76, 72, 60, 0, 100, 100, 100, 
88, 50, 85, 76, 94, 0, 67, 78, 89, 56, 45, 76, 80, 82, 73, 91, 64, 55, 76, 94, 84, 
73, 63, 52, 76, 81, 76, 66, 88, 77, 99, 76, 25, 76, 76, 100, 90, 76, 88, 94, 
82, 93, 87, 95, 81, 89, 92, 85, 96, 91, 84, 99, 86, 98, 97, 83, 76, 50, 76, 100, 
76, 0, 80, 94, 93, 65, 100, 75, 95, 76, 72, 60, 0, 100, 100, 100, 88, 50, 85, 76, 
94, 0, 67, 78, 89, 56, 45, 76, 80, 82, 73, 91, 64, 55, 76, 94, 84, 73, 63, 52, 76, 
81, 76, 66, 88, 77, 99, 76] 

section02 = [25, 76, 76, 100, 90, 76, 70, 88, 94, 82, 93, 87, 95, 81, 89, 92, 85, 
96, 91, 84, 99, 86, 98, 97, 83, 76, 50, 76, 67, 71, 78, 68, 69, 74, 61, 1, 62, 
72, 66, 20, 75, 91, 30, 100, 100, 40, 76, 74, 63, 75, 64, 77, 70, 65, 79, 60, 100, 
76, 0, 80, 94, 93, 65, 100, 75, 95, 76, 72, 60, 0, 5, 59]

section05 = [76, 100, 76, 88, 50, 85, 76, 94, 0, 67, 78, 89, 56, 45, 76, 80, 82, 
73, 91, 64, 55, 76, 94, 84, 73, 63, 52, 76, 81, 76, 66, 88, 77, 99, 76, 25, 76, 76, 
100, 90, 76, 70, 88, 94, 82, 93, 87, 95, 81, 89, 92, 85, 96, 91, 84, 99, 86, 98, 
97, 83, 76, 50, 76, 100, 76, 0, 80, 94, 93, 65, 100, 75, 95, 76, 72, 60, 0, 100, 
100, 100, 88, 50, 85, 76, 94, 0, 67, 78, 89, 56, 45, 76, 80, 82, 73, 91, 64, 55, 
76, 94, 84, 73, 63, 52, 76, 81, 76, 66, 88, 77, 99, 76, 76, 76, 100, 90, 76, 
70, 88, 94, 82, 93, 87, 95, 81, 89, 92, 85, 96, 91, 84, 99, 86, 98, 97, 83, 76, 50, 
76, 67, 73,71, 78, 68, 69, 74, 61, 62, 72, 66, 76, 74, 63, 75, 64, 77, 70, 65, 79, 
60, 76, 76, 76, 76]

print("There are", unique_grades(section01), "different grades in Section 01") #There are 40 different grades in Section 01
print("There are", unique_grades(section02), "different grades in Section 02") #There are 49 different grades in Section 02
print("There are", unique_grades(section05), "different grades in Section 05") #There are 48 different grades in Section 05
print("There are", combine_sections_size(section01, section02, section05), "different students") #There are 361 different students
print("There are", len(course_set(section01, section02, section05)),"unique grades in all sections") #There are 54 unique grades in all sections
#It is important here that the input is set to an integer. Otherwise it would be read as a string and the search_grades function wouldn't work.
search = int(input("Please enter a grade you wish to search for within the classes "))
print(search_grades(section01, section02, section05, search)) #True or False depending on what number you entered
print("The grades that appeared in all sections are: ", common_grades(section01, section02, section05)) 
#The grades that appeared in all sections are: {0, 25, 50, 60, 63, 64, 65, 66, 67, 72, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100}