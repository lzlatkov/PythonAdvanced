from collections import deque

liters = int(input())
name = input()
line = deque()

while name != "Start":
    line.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        customer = line.popleft()
        liters_wanted = int(command)
        if liters_wanted <= liters:
            liters -= liters_wanted
            print(f"{customer} got water")
        else:
            print(f"{customer} must wait")
    else:
        refill, refilled_liters = command.split()
        refilled_liters = int(refilled_liters)
        liters += refilled_liters
    command = input()

print(f"{liters} liters left")