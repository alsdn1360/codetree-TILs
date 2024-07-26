n = int(input())

arr = list(map(int, input().split()))

minDiffernt = 100

for i in range(n):
    for j in range(i + 1, n):
          if arr[j] - arr[i] < minDiffernt:
            minDiffernt = arr[j] - arr[i]

print(minDiffernt)