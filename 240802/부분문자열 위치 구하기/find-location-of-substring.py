word = input()
target = input()

if target in word:
    print(word.index(target))
else:
    print('-1')