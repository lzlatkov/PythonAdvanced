row_count = int(input())
matrix = []
flat_list = []
for row in range(row_count):
    row_data = [int(num) for num in input().split(", ")]
    flat_list.extend(row_data)
# flat_list = [element for row in matrix for element in row]


print(flat_list)