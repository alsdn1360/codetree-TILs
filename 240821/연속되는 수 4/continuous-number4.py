N = int(input())
arr = []
cnt = 0
max_cnt = 0

for _ in range(N):
    num = int(input())
    arr.append(num)

for i in range(N):
    if arr[i] < arr[i - 1]:
        cnt = 1
    elif i == 0 or arr[i] > arr[i - 1]:
        cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)