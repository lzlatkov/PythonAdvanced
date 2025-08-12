rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

element_sum = 0

for el in matrix:
    element_sum += sum(el)

print(element_sum)
print(matrix)