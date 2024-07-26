arr2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

totalSum = 0

for i in range(4):
    for j in range(i + 1):
        totalSum += arr2d[i][j]

print(totalSum)