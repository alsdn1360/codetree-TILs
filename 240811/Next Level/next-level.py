class user_info():
    def __init__(self, id = 'codetree', lv = 10):
        self.id = id
        self.lv = lv

second_user_id, second_user_lv = tuple(input().split())

first_user = user_info()
second_user = user_info(second_user_id, int(second_user_lv))

print(f'user {first_user.id} lv {first_user.lv}')
print(f'user {second_user.id} lv {second_user.lv}')