word = input()
rle = []

sameAlpha = word[0]
cnt = 1

rle.append(sameAlpha)

for i in range(1, len(word)):
    rle.append(word[i])

    if sameAlpha == word[i]:
        cnt += 1
        rle.pop()

        if i == len(word) - 1:
            rle.append(cnt)
    else:
        rle.pop()
        rle.append(cnt)
        rle.append(word[i])

        sameAlpha = word[i]
        cnt = 1

print(len(rle))

for i in rle:
    print(i, end = '')