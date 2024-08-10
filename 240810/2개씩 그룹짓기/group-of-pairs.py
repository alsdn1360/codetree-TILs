n = int(input())
arr = list(map(int, input().split()))

arr.sort()
max_val = 0

for i in range(n):
    temp_val = arr[i] + arr[len(arr) - 1 - i]

    if max_val < temp_val:
        max_val = temp_val

print(max_val)