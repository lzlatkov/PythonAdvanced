my_stack = []

numbers_count = int(input())

for _ in range(numbers_count):
    numbers = [int(x) for x in input().split()]
    query = numbers[0]
    if query == 1:
        my_stack.append(int(numbers[1]))
    elif query == 2:
        if my_stack:
            my_stack.pop()
    elif query == 3:
        if my_stack:
            print(max(my_stack))
    elif query == 4:
        if my_stack:
            print(min(my_stack))

my_stack.reverse()

print(*my_stack, sep=", ")

