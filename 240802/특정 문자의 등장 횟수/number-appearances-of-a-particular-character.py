word = input()

cnt_ee = 0
cnt_eb = 0

for i in range(len(word)):
    if word[i:i+2] == 'ee':
      cnt_ee += 1

    if word[i:i+2] == 'eb':
      cnt_eb += 1

print(f'{cnt_ee} {cnt_eb}')