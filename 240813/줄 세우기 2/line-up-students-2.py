class Student():
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

n = int(input())
students = []
idx = 1

for _ in range(n):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, idx))
    idx += 1


students.sort(key = lambda x : (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.idx)