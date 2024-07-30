arr = [
    input()
    for _ in range(10)
]

alpha = input()

for word in arr:
    if word[len(word) - 1] == alpha:
        print(word)