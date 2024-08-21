N, M, K = tuple(map(int, input().split()))
students_penalty = [0] * (N + 1)
penalty = []

for i in range(M):
    target = int(input())

    students_penalty[target] += 1

    if students_penalty[target] >= K:
        penalty.append(target)

if len(penalty) == 0:
    print('-1')
else:
    print(penalty[0])