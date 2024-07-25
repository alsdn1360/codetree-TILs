n = int(input())
arr = list(map(int,input().split()))

cntMin = 0

for i in range(n):
    if min(arr) == arr[i]:
        cntMin += 1

print(f'{min(arr)} {cntMin}')