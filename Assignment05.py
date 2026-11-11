# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: Course registration using dictionaries, JSON files, and exception handling
# Change Log: (Who, When, What)
#   Theresa Dryden,11/11/2026,Created Script
# ------------------------------------------------------------------------------------------ #
import json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''
FILE_NAME: str = 'Enrollments.json'
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
menu_choice: str = ''
student_data: dict = {}
students: list = []
file = None

# Read saved records into a list of dictionaries.
try:
    file = open(FILE_NAME, 'r', encoding='utf-8')
    students = json.load(file)
    if not isinstance(students, list):
        raise ValueError('Enrollment data must be a list.')
    for student in students:
        if not isinstance(student, dict):
            raise ValueError('Each enrollment must be a dictionary.')
        for key in ('FirstName', 'LastName', 'CourseName'):
            if key not in student:
                raise ValueError(f'Missing required key: {key}')
except FileNotFoundError:
    print('Enrollment file not found. Starting with no registrations.')
    students = []
except (OSError, json.JSONDecodeError, ValueError) as error:
    print(f'Unable to load enrollment data: {error}')
    students = []
finally:
    if file is not None and not file.closed:
        file.close()

while True:
    print(MENU)
    menu_choice = input('What would you like to do: ').strip()

    if menu_choice == '1':
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError('First name cannot be blank.')
        except (ValueError, EOFError) as error:
            print(f'Invalid first name: {error}')
            continue
        try:
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError('Last name cannot be blank.')
        except (ValueError, EOFError) as error:
            print(f'Invalid last name: {error}')
            continue
        try:
            course_name = input('Please enter the name of the course: ').strip()
            if not course_name:
                raise ValueError('Course name cannot be blank.')
        except (ValueError, EOFError) as error:
            print(f'Invalid course name: {error}')
            continue
        student_data = {
            'FirstName': student_first_name,
            'LastName': student_last_name,
            'CourseName': course_name
        }
        students.append(student_data)
        print(f'You have registered {student_first_name} '
              f'{student_last_name} for {course_name}.')

    elif menu_choice == '2':
        print('-' * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in '
                  f'{student["CourseName"]}')
        print('-' * 50)

    elif menu_choice == '3':
        try:
            file = open(FILE_NAME, 'w', encoding='utf-8')
            json.dump(students, file, indent=4)
            print('The following data was saved to file!')
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in '
                      f'{student["CourseName"]}')
        except (OSError, TypeError) as error:
            print(f'Unable to save enrollment data: {error}')
        finally:
            if file is not None and not file.closed:
                file.close()

    elif menu_choice == '4':
        break
    else:
        print('Please only choose option 1, 2, 3, or 4')

print('Program Ended')
