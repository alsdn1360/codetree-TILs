arr2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

widthSum = 0
heightSum = 0
totalSum = 0

for i in range(2):
    for j in range(4):
        widthSum += arr2d[i][j]
        totalSum += arr2d[i][j]
    
    print(f'{widthSum / 4:.1f}', end = ' ')
    widthSum = 0

print()

for i in range(4):
    for j in range(2):
        heightSum += arr2d[j][i]
    
    print(f'{heightSum / 2:.1f}', end = ' ')
    heightSum = 0

print(f'\n{totalSum / 8:.1f}')