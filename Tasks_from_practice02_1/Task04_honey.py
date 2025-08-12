from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0


def calculate(b, n, o):
    if o == "+":
        return abs(b + n)
    elif o == "-":
        return abs(b - n)
    elif o == "*":
        return abs(b * n)
    elif o == "/":
        if n == 0:
            return 0
        else:
            return abs(b / n)


while bees and nectar:
    if nectar[-1] >= bees[0]:
        op = symbols.popleft()
        bee = bees.popleft()
        nec = nectar.pop()
        total_honey += calculate(bee, nec, op)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
