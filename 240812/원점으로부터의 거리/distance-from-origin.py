class Point():
    def __init__(self, distance, number):
        self.distance = distance
        self.number = number

n = int(input())

number = 0
points = []
for _ in range(n):
    x, y = tuple(map(int, input().split()))

    distance = abs(x) + abs(y)
    number += 1

    points.append(Point(distance, number))

points.sort(key = lambda x : (x.distance, x.number))

for point in points:
    print(point.number)