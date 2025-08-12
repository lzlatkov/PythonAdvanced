from collections import deque

#Read user input
materials = [int(m) for m in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {}
items = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
# Logic
while materials and magic_level:
    current_magic = materials[-1] * magic_level[0]
    if current_magic in items:
        current_present = items[current_magic]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
        materials.pop()
        magic_level.popleft()
    elif current_magic < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif current_magic not in items and current_magic > 0:
        magic_level.popleft()
        materials[-1] += 15
    elif current_magic == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()

# Print output
if ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials[::-1]])}")
if magic_level:
    print(f"Magic left: {', '.join([str(m) for m in magic_level])}")
for key, value in sorted(presents.items()):
    print(f"{key}: {value}")