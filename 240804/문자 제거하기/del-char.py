word = input()
arr = list(word)

iter = len(word) - 1

for i in range(iter):
    remove = int(input())

    if remove > len(arr):
        remove = len(arr) - 1

    arr.pop(remove)

    word = ''.join(arr)

    for j in range(len(arr)):
        print(arr[j], end = '')

    print()