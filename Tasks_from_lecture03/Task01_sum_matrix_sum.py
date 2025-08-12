rows, columns = [int(num) for num in input().split(", ")]
matrix = []

for row in range(rows):
    row_data =[int(el) for el in input().split(", ")]
    matrix.append(row_data)

elements_sum = 0
for row_data in matrix:
    elements_sum += sum(row_data)

print(elements_sum)
print(matrix)


