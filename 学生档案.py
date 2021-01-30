import random as rd

students = []

for x in range(10) :
    name = '小' + chr(ord('A') + x)
    student = {
        'name' : name,
        'id' : 201900 + x,
        'score' : rd.randint(60,100)
    }
    students.append(student)

print(students)

students.sort(key = lambda x : x['score'],reverse = False)

for student in students:
    print(student['id'],student['name'],student['score'])

