class person_info():
    def __init__(self, name, street, location):
        self.name = name
        self.street = street
        self.location = location

n = int(input())

people = []
for _ in range(n):
    name, street, location = tuple(input().split())
    people.append(person_info(name, street, location))

min_idx = 0
for i in range(1, n):
    if people[min_idx].name > people[i].name:
        min_idx = i

print(f'name {people[i].name}\naddr {people[i].street}\ncity {people[i].location}')