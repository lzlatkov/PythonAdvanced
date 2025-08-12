from collections import deque

total_clothes = deque(int(x) for x in input().split())
total_capacity = int(input())

current_rack_capacity = total_capacity
racks = 1

while total_clothes:
    clothing = total_clothes.pop()
    if current_rack_capacity >= clothing:
        current_rack_capacity -= clothing
    else:
        racks += 1
        current_rack_capacity = total_capacity - clothing

print(racks)


