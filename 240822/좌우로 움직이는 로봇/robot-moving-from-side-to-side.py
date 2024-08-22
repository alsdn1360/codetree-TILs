n, m = tuple(map(int, input().split()))

A = [0]
B = [0]

for i in range(n):
    t, d = tuple(input().split())
    t = int(t)

    if d == 'R':
        for _ in range(t):
            A.append(A[-1] + 1)
    else:
        for _ in range(t):
            A.append(A[-1] - 1)

for i in range(m):
    t, d = tuple(input().split())
    t = int(t)

    if d == 'R':
        for _ in range(t):
            B.append(B[-1] + 1)
    else:
        for _ in range(t):
            B.append(B[-1] - 1)

if len(A) > len(B):
    for _ in range(len(A) - len(B)):
        B.append(B[-1])
elif len(A) < len(B):
    for _ in range(len(B) - len(A)):
        A.append(A[-1])

same_place_cnt = 0

for i in range(1, min(len(A), len(B))):
    if A[i - 1] != B[i - 1] and A[i] == B[i]:
        same_place_cnt += 1

print(same_place_cnt)