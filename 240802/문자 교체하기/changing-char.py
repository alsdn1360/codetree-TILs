word1, word2 = input().split()

arr1 = list(word1)
arr2 = list(word2)

word1 = ''.join(arr1[:2])
word2 = ''.join(arr2[2:])

result = word1 + word2

print(result)