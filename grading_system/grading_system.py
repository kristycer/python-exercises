from statistics import mean as m

admins = {'John': 'Pass123', 'me': '123'}
studentDict = {'Tom': [60, 78, 90],
               'Mia': [69, 74, 70],
               'Josh': [70, 80, 40],}
def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')
    print(studentDict)

def removeStudent():
    nameToRemove = input('What student to remove?: ')
    if nameToRemove in studentDict:
        del studentDict[nameToRemove]
    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent, 'has an average grade of:', avgGrade)
def main():
    print("""
Welcome to Grade central
[1] - Enter Grades
[2] - Remove Student
[3] - Student Average Grades
[4] - Exit
    """)

    action = input("What would you like to do today? (Enter a number)")

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again!')


login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome, ', login)
        while True:
            main()
    else:
        print('Invalid password!')
else:
    print('Invalid username!')