matrix = [[int(el) for el in input().split(", ")] for row in range(int(input()))]
main_diagonal_list = []
secondary_diagonal_list = []

for row, column in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[row][row]
    b = matrix[row][column]
    main_diagonal_list.append(a)
    secondary_diagonal_list.append(b)

print(f"Primary diagonal: {', '.join(str(el) for el in main_diagonal_list)}. Sum: {sum(main_diagonal_list)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal_list)}. Sum: {sum(secondary_diagonal_list)}")
