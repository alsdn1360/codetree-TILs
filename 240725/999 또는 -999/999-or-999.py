arr = list(map(int, input().split()))

if 999 in arr:
    endIndex = arr.index(999)
elif -999 in arr:
    endIndex = arr.index(-999)

newArr = []

for i in range(endIndex):
    newArr.append(arr[i])

print(f'{max(newArr)} {min(newArr)}')