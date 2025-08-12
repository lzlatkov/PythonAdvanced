number_of_commands = int(input())
cars = set()

for _ in range(number_of_commands):
    command, number = input().split(", ")
    if command == "IN":
        cars.add(number)
    elif command == "OUT":
        cars.remove(number)

if cars:
    print(*cars, sep='\n')
else:
    print("Parking Lot is Empty")
