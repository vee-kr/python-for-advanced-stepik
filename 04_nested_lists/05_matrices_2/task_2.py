rows, columns = int(input()), int(input())
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

max_elem, max_row, max_column = matrix[0][0], 0, 0

for r in range(rows):
    for c in range(columns):
        if matrix[r][c] > max_elem:
            max_elem = matrix[r][c]
            max_row = r
            max_column = c
            
print(max_row, max_column)
