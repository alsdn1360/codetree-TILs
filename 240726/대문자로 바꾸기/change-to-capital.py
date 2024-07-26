arr2d = []

for i in range(5):
    arr1d = list(input().split())
    arr2d.append(arr1d)

for i in arr2d:
    for j in i:
        print(j.upper(), end = ' ')
    
    print()