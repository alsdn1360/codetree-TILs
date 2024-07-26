firstArr2d = [
    list(map(int, input().split()))
    for _ in range(3)
]
input()
secondArr2d = [
    list(map(int, input().split()))
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        print(firstArr2d[i][j] * secondArr2d[i][j], end = ' ')

    print()