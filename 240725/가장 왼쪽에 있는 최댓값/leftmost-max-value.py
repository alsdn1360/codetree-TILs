n = int(input())

arr = list(map(int, input().split()))

maxIndex = 1

while(maxIndex > 0):
    maxIndex = arr.index(max(arr))

    print(maxIndex + 1, end = ' ')

    del arr[maxIndex:]