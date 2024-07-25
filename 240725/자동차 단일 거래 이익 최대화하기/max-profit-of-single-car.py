n = int(input())

arr = list(map(int, input().split()))

buyYear = 0
buy = 0
sellYear = 0
sell = 0

buyYear = arr.index(min(arr))
buy = arr[buyYear]

del arr[0:buyYear]

sellYear = arr.index(max(arr))
sell = arr[sellYear]

print(sell - buy)