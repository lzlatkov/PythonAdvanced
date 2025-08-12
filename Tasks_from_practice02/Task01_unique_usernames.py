username_set = set()

names = int(input())
for _ in range(names):
    name = input()
    username_set.add(name)

print(*username_set, sep='\n')