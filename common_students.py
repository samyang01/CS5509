#lab1_assignment4
#compare the lists of students in two different classes 1. "python" and 2. "web applications"
#find the students that are taking both classes and print the list
#next, find the students that are only taking one class but not the other and print the list

python_students=[]
web_students=[]
common_students=[]
disjoint_students=[]

print('enter names of students in the python class, press enter when done')
while True:
    name=input()
    python_students.append(name)
    if name == '':
        break


print('enter names of students in the web applications class, press enter when done')
while True:
    name=input()
    web_students.append(name)
    if name == '':
        break


'''check to see if students are in both python and web applications class
use a for loop to check to see if each student in python is also in web applications.
If students are in both classes then append to 'common students' list.  If students
are not in boh classes then append to 'disjoint students' list'''
for student in python_students:
    if student in web_students:
        common_students.append(student)
    else:
        disjoint_students.append(student)
'''since we already checked the python student list for students taking both classes, we
only need to check the web application student list for students not taking both classes and 
append to 'disjoint student list'''
for student in web_students:
    if student not in python_students:
        disjoint_students.append(student)
print('students taking both classes are\n' +str(common_students[:-1]))
print('students taking only one class are\n'+str(disjoint_students[:]))
