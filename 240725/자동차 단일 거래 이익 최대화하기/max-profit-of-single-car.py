n = int(input())

arr = list(map(int, input().split()))

buyYear = 0
buy = 0
sellYear = 0
sell = 0

buyYear = arr.index(min(arr))
buy = arr[buyYear]

del arr[:buyYear]

sellYear = arr.index(max(arr))
sell = arr[sellYear]

gain = sell - buy

if gain > 0:
    print(gain)
else:
    print('0')