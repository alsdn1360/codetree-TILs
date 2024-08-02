s, q = input().split()

word = list(s)
q = int(q)
temp = ''

for i in range(q):
    query = list(input().split())

    if query[0] == '1':
        a = int(query[1]) - 1
        b = int(query[2]) - 1

        temp = word[a]
        word[a] = word[b]
        word[b] = temp

        s = ''.join(word)
        print(s)

        word = list(s)
    else:
        for j in range(len(word)):
            if word[j] == query[1]:
                word[j] = query[2]
            
        s = ''.join(word)
        print(s)

        word = list(s)