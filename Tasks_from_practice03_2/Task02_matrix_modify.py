matrix = [[int(el) for el in input().split()]for _ in range(int(input()))]


while True:
    command = input().split()
    cmd = command[0]
    if cmd == "END":
        break
    row = int(command[1])
    column = int(command[2])
    number = int(command[3])

    if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix):
        print(f"Invalid coordinates")
        continue
    if cmd == "Add":
        matrix[row][column] += number
    elif cmd == "Subtract":
        matrix[row][column] -= number

for row in matrix:
    print(*row)