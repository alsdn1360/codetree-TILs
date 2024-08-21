A = [0]
B = [0]

N, M = tuple(map(int, input().split()))

for _ in range(N):
    d, t = tuple(input().split())
    t = int(t)

    if d == 'R':
        for i in range(1, t + 1):
            A.append(A[-1] + 1)
    elif d == 'L':
        for i in range(1, t + 1):
            A.append(A[-1] - 1)

for _ in range(M):
    d, t = tuple(input().split())
    t = int(t)

    if d == 'R':
        for i in range(1, t + 1):
            B.append(B[-1] + 1)
    elif d == 'L':
        for i in range(1, t + 1):
            B.append(B[-1] - 1)

first_meet = -1

for i in range(1, min(len(A), len(B))):
    if A[i] == B[i]:
        first_meet = i
        break
        
print(first_meet)