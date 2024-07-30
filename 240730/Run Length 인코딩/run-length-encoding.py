word = input()
rle = []

sameAlpha = word[0]
cnt = 0

rle.append(sameAlpha)

for i in range(len(word)):
    rle.append(word[i])

    if sameAlpha == word[i]:
        cnt += 1
        rle.pop()
    else:
        rle.pop()
        rle.append(cnt)
        rle.append(word[i])

        sameAlpha = word[i]
        cnt = 1
    
    if i == len(word) - 1:
        rle.append(cnt)

result = ''.join(str(word) for word in rle)

print(len(result))
print(result)