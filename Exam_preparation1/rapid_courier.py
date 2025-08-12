from collections import deque
# Read user input
packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])
total_delivered_weight = 0

# Logic
while packages and couriers:
    last_package = packages[-1]
    first_courier = couriers[0]

    if first_courier >= last_package:
        capacity = first_courier - last_package * 2
        couriers.popleft()
        if capacity > 0:
            couriers.append(capacity)
        total_delivered_weight += packages.pop()
    else:
        packages[-1] -= couriers.popleft()
        total_delivered_weight += first_courier

# Print output
print(f"Total weight: {total_delivered_weight} kg")

if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages)}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} but there are no more packages to deliver.")
