presents_count = int(input())
n = int(input())
matrix = []
santa = []
nice_kids_count = 0
nice_kids_gifted = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids_count += 1

directions = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

while presents_count > 0:
    command = input()
    if command == "Christmas morning":
        break
    row, col = santa[0] + directions[command][0], santa[1] + directions[command][1]
    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "V":
            presents_count -= 1
            nice_kids_gifted += 1
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            for direction in directions.values():
                next_row, next_col = row + direction[0], col + direction[1]
                if matrix[next_row][next_col] in "VX" and presents_count > 0:
                    presents_count -= 1
                    if matrix[next_row][next_col] == "V":
                        nice_kids_gifted += 1
                    matrix[next_row][next_col] = "-"
        matrix[santa[0]][santa[1]] = "-"
        santa = [row, col]
        matrix[row][col] = "S"

if presents_count < 1 and nice_kids_count - nice_kids_gifted > 0:
    print(f"Santa ran out of presents!")
for row in matrix:
    print(*row)
if nice_kids_count - nice_kids_gifted > 0:
    print(f"No presents for {nice_kids_count - nice_kids_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")
