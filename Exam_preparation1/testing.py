from collections import deque

packages= [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])
total_delivered = 0

while packages and couriers:
    current_package = packages.pop()
    current_courier = couriers.popleft()
    if current_courier >= current_package:
        capacity = current_courier - current_package * 2
        if capacity > 0:
            couriers.append(capacity)
        total_delivered += current_package
    else:
        current_package -= current_courier
        packages.append(current_package)
        total_delivered += current_package

print(f"Total weight: {total_delivered} kg")
if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {','.join([str(x) for x in packages])}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join([str(x) for x in couriers])} but there are no more packages to deliver.")