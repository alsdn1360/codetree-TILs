word = input()
arr = list(word)

for i in range(len(word) - 1):
    remove = int(input())

    if remove > len(arr):
        remove = len(arr) - 1

    arr.pop(remove)

    word = ''.join(arr)

    for j in range(len(arr)):
        print(arr[j], end = '')

    print()