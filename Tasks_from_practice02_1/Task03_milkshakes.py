from collections import deque

choco = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
total = 0

while choco and milk and total < 5:

    if choco[-1] <= 0 and milk[0] <= 0:
        choco.pop()
        milk.popleft()
        continue
    if choco[-1] <= 0:
        choco.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if choco[-1] == milk[0]:
        total += 1
        choco.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        choco[-1] -= 5

if total == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
if choco:
    print(f"Chocolate: {', '.join([str(x) for x in choco])}")
else:
    print(f"Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print(f"Milk: empty")