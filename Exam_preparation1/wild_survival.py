from collections import deque
# Read user input
bees = deque([int(x) for x in input().split()])
bee_eaters = [int(x) for x in input().split()]
bees_killed_by_bee_eater = 7
# Logic
while bees and bee_eaters:
    current_bees = bees.popleft()
    current_bee_eater = bee_eaters.pop()

    while current_bees > 0 and current_bee_eater > 0:
        current_bees -= bees_killed_by_bee_eater
        if current_bees > 0:
            current_bee_eater -= 1
    if current_bees > 0:
        bees.append(current_bees)

    elif current_bee_eater > 0:
        bee_eaters.append(current_bee_eater)


print(f"The final battle is over!")

if bees:
    print(f"Bee groups left: {', '.join([str(x) for x in bees])}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join([str(x) for x in bee_eaters])}")
else:
    print(f"But no one made it out alive!")

