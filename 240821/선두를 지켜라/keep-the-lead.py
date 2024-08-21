N, M = tuple(map(int, input().split()))

A = [0]
B = [0]
first_person = []

for _ in range(N):
    v, t = tuple(map(int, input().split()))

    for _ in range(1, t + 1):
        A.append(A[-1] + v)

for _ in range(M):
    v, t = tuple(map(int, input().split()))

    for _ in range(1, t + 1):
        B.append(B[-1] + v)

for i in range(1, len(A)):
    if A[i] > B[i]:
        first_person.append('A')
    elif A[i] < B[i]:
        first_person.append('B')
    else:
        first_person.append('N')

while 'N' in first_person:
    first_person.remove('N')

change_first_cnt = 0

for i in range(1, len(first_person)):
    if first_person[i] != first_person[i - 1]:
        change_first_cnt += 1

print(change_first_cnt)