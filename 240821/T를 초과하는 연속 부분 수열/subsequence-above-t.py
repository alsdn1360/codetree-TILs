n, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

cnt = 0
max_cnt = 0

for i in range(n):
    if arr[i] <= t:
        cnt = 0
    elif i == 0 or arr[i] > t:
        cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)