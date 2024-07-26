n, m = map(int, input().split())

num = 1

numArr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        numArr[i][j] = num
        num += 1

        print(numArr[i][j], end = ' ')

    print()