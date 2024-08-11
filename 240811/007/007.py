class mission:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

word = list(input().split())

mission_007 = mission(word[0], word[1], word[2])

print(f'secret code : {mission_007.code}')
print(f'meeting point : {mission_007.point}')
print(f'time : {mission_007.time}')