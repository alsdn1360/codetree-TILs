arr = list(map(int, input().split()))

endIndex = arr.index(999 or -999)

newArr = []

for i in range(endIndex):
    newArr.append(arr[i])

print(f'{max(newArr)} {min(newArr)}')