word = input()

arr = list(word)

arr.pop(1)
arr.pop(-2)

word = ''.join(arr)

print(word)