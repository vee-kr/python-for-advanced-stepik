num_rows_columns = int(input())
matrix = [[0] * num_rows_columns for _ in range(num_rows_columns)]
for r in range(num_rows_columns):
    for c in range(num_rows_columns):
        matrix[r][r] = 1
        matrix[r][num_rows_columns - r - 1] = 1
        if (r < c < num_rows_columns- 1 - r) or (num_rows_columns - 1 - r < c < r):
            matrix[r][c] = 1
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=' ')
    print()
