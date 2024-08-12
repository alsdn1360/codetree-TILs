class Student():
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

students = []
number = 0
for _ in range(n):
    height, weight = tuple(map(int, input().split()))
    number += 1
    students.append(Student(height, weight, number))

students.sort(key = lambda x : (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)