number_of_students = int(input())
students_dictionary = {}

for _ in range(number_of_students):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_dictionary:
        students_dictionary[student] = []
    students_dictionary[student].append(grade)

for student_name, grades in students_dictionary.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student_name} -> {' '.join([f'{(el):.2f}' for el in grades])} (avg: {average_grade:.2f})")
