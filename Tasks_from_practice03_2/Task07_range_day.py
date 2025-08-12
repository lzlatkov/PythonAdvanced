SIZE = 5

matrix = []
targets = 0
current_position = []
for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            current_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

direction = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}
targets_shot = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "shoot":
        row = current_position[0] + direction[command[1]][0]
        col = current_position[1] + direction[command[1]][1]
        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets -= 1
                targets_shot.append([row, col])
                break
            row += direction[command[1]][0]
            col += direction[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_shot)} targets hit.")
            break

    elif command[0] == "move":
        row = current_position[0] + direction[command[1]][0] * int(command[2])
        col = current_position[1] + direction[command[1]][1] * int(command[2])
        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == ".":
            matrix[row][col] = "A"
            matrix[current_position[0]][current_position[1]] = "."
            current_position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for row in targets_shot:
    print(row)
