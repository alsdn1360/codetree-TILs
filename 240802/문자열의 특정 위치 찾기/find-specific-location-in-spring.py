word, target = input().split()

if target in word:
    print(word.index(target))
else:
    print('No')