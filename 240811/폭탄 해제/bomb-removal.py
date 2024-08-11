class bomb():
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = tuple(input().split())

bomb_info = bomb(code, color, int(second))

print(f'code : {bomb_info.code}\ncolor : {bomb_info.color}\nsecond : {bomb_info.second}')