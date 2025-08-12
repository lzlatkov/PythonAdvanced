# Read user input
n, m = [int(x) for x in input().split(", ")]

matrix = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), "defuse": (0, 0)}
seconds_remaining = 16

counter_terrorist_position = []
bomb_position = []
no_time_remaining = False
bomb_defused = False
killed = False
bomb_exploded = False
next_row = 0
next_col = 0
initial_counter_terrorist_position = []
# Logic
for row in range(n):
    row_data = input()
    matrix.append(list(row_data))

    if "C" in row_data:
        counter_terrorist_position = [row, row_data.index("C")]
        initial_counter_terrorist_position = [row, row_data.index("C")]
        matrix[row][row_data.index("C")] = "*"
    if "B" in row_data:
        bomb_position = [row, row_data.index("B")]

while True:
    command = input()
    if seconds_remaining <= 0:
        no_time_remaining = True
        break

    current_row = counter_terrorist_position[0]
    current_col = counter_terrorist_position[1]

    if command in possible_moves:
        if command == "up":

            next_row = current_row + possible_moves[command][0]
            next_col = current_col + possible_moves[command][1]
            if next_row not in range(n) or next_col not in range(m):
                seconds_remaining -= 1
                continue
            seconds_remaining -= 1
            counter_terrorist_position = [next_row, next_col]
        elif command == "down":
            next_row = current_row + possible_moves[command][0]
            next_col = current_col + possible_moves[command][1]
            if next_row not in range(n) or next_col not in range(m):
                seconds_remaining -= 1
                continue
            seconds_remaining -= 1
            counter_terrorist_position = [next_row, next_col]
        elif command == "left":
            next_row = current_row + possible_moves[command][0]
            next_col = current_col + possible_moves[command][1]
            if next_row not in range(n) or next_col not in range(m):
                seconds_remaining -= 1
                continue
            seconds_remaining -= 1
            counter_terrorist_position = [next_row, next_col]
        elif command == "right":
            next_row = current_row + possible_moves[command][0]
            next_col = current_col + possible_moves[command][1]
            if next_row not in range(n) or next_col not in range(m):
                seconds_remaining -= 1
                continue
            seconds_remaining -= 1
            counter_terrorist_position = [next_row, next_col]
        elif command == "defuse":
            if counter_terrorist_position == bomb_position:
                if seconds_remaining >= 4:
                    seconds_remaining -= 4
                    bomb_defused = True
                    matrix[bomb_position[0]][bomb_position[1]] = "D"
                    break
                else:
                    bomb_exploded = True
                    matrix[bomb_position[0]][bomb_position[1]] = "X"
                    break
            else:
                seconds_remaining -= 2
    if matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] == "T":
        matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] = "*"
        killed = True
        break

if killed:
    print("Terrorists win!")
elif bomb_defused:
    print(f"Counter-terrorist wins!")
    print(f"Bomb has been defused: {seconds_remaining} second/s remaining.")
else:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    if no_time_remaining:
        print(f"Time needed: 0 second/s.")
    elif bomb_exploded:
        print(f"Time needed: {abs(seconds_remaining - 4)} second/s.")

matrix[initial_counter_terrorist_position[0]][initial_counter_terrorist_position[1]] = "C"

for row in matrix:
    print("".join(row))
