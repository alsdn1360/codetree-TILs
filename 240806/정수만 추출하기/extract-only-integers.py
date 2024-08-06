a, b = input().split()

a = list(a)
b = list(b)

arr_a = []
arr_b = []

for i in range(len(a)):
    if ord(a[i]) < 49 or ord(a[i]) > 57:
        break
    arr_a.append(a[i])
    
for i in range(len(b)):
    if ord(b[i]) < 49 or ord(b[i]) > 57:
        break
    arr_b.append(b[i])

arr_a = ''.join(arr_a)
arr_b = ''.join(arr_b)

print(int(arr_a) + int(arr_b))