#Read user input
first_input = set([int(x) for x in input().split()])
second_input = set([int(x) for x in input().split()])
n = int(input())
#Logic
for i in range(n):
    user_input = input().split()
    command = f"{user_input[0]} {user_input[1]}"
    numbers = [int(number) for number in user_input[2:]]
    if command == "Add First":
        first_input.update(numbers)
    elif command == "Add Second":
        second_input.update(numbers)
    elif command == "Remove First":
        first_input.difference_update(numbers)
    elif command == "Remove Second":
        second_input.difference_update(numbers)
    elif command == "Check Subset":
        if first_input.issubset(second_input) or second_input.issubset(first_input):
            print("True")
        else:
            print("False")

#Print output
print(*sorted(first_input), sep=", ")
print(*sorted(second_input), sep=", ")