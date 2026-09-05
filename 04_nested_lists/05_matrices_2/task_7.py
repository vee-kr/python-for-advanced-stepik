num_rows_columns = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num_rows_columns)]

new_matrix = []
for c in range(num_rows_columns):
    row = []
    for r in range(num_rows_columns-1, -1, -1):
        row.append(matrix[r][c])

    new_matrix.append(row)

for rows in new_matrix:
    print(*rows)
    

