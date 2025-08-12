directions = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}


def calculate_position(direction, directions, current_row_index, current_col_index, n):
    next_row_index = current_row_index + directions[direction][0]
    next_col_index = current_col_index + directions[direction][1]

    next_row_index = next_row_index % n
    next_col_index = next_col_index % n
    return next_row_index, next_col_index


n = int(input())
nectar = 0
matrix = []
bee_position = None
initial_energy = 15
restored_energy = False

for row_index in range(n):
    row_data = list(input())
    if "B" in row_data:
        col_index = row_data.index("B")
        bee_position = (row_index, col_index)
    matrix.append(row_data)
while True:
    command = input()

    current_row_index, current_col_index = bee_position
    next_row_index, next_col_index = calculate_position(command, directions, current_row_index, current_col_index, n)

    landing_index = matrix[next_row_index][next_col_index]
    matrix[current_row_index][current_col_index] = "-"
    matrix[next_row_index][next_col_index] = "B"
    bee_position = (next_row_index, next_col_index)
    initial_energy -= 1

    if landing_index.isdigit():
        nectar += int(landing_index)

    elif landing_index == "H":
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if initial_energy <= 0 and nectar < 30:
        print(f"This is the end! Beesy ran out of energy.")
        break

    if initial_energy <= 0 and nectar >= 30 and not restored_energy:
        diff = nectar - 30
        initial_energy += diff
        nectar = 30
        restored_energy = True

for row in matrix:
    print(*row, sep="")


