from collections import deque

total_food = int(input())
food_orders = deque([int(x) for x in input().split()])

print(max(food_orders))

for order in food_orders.copy():
    if order <= total_food:
        food_orders.popleft()
        total_food -= order
    else:
        print(f"Orders left: {' '.join(str(x) for x in food_orders)}")
        break
else:
    print("Orders complete")