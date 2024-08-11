class item():
    def __init__(self, name, code):
        self.name = name
        self.code = code

second_item_name, second_item_code = tuple(input().split())

first_item = item('codetree', 50)
second_item = item(second_item_name, int(second_item_code))

print(f'product {first_item.code} is {first_item.name}\nproduct {second_item.code} is {second_item.name}')