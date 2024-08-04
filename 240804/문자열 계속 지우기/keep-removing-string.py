A = input()
B = input()

while(1):
    if B in A:
        B_remove = A.find(B)

        arr_A = list(A)

        for j in range(len(B)):
            arr_A.pop(B_remove)

        A = ''.join(arr_A)
    else:
        break

print(A)