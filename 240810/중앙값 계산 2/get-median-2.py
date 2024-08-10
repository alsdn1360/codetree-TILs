n = int(input())
num = list(map(int, input().split()))

odd_num = []

for i in range(n):
    odd_num.append(num[i])

    if i % 2 == 0:
        odd_num.sort()
        central_index = len(odd_num) // 2

        print(odd_num[central_index], end = ' ')