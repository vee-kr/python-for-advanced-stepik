num_rows_columns = int(input())
matrix = [['.' for _ in range(num_rows_columns)] for _ in range(num_rows_columns)]
for r in range(num_rows_columns):
    for c in range(num_rows_columns):
        matrix[r][num_rows_columns - 1 - r] = 1
        if c < (num_rows_columns - 1 -r):
            matrix[r][c] = 0
        elif c > (num_rows_columns - 1 - r):
            matrix[r][c] = 2

for row in matrix:
    print(*row)
