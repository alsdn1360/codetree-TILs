n , m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1

for diagonal in range(n + m - 1):
    if diagonal < m:
        for i in range(min(diagonal + 1, n)):
            arr[i][diagonal - i] = cnt
            cnt += 1
    else:
        for i in range(diagonal - m + 1,  m):
            arr[i][diagonal - i] = cnt
            cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()