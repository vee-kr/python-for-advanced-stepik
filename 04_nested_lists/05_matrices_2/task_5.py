num_rows_columns = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num_rows_columns)]

for r in range(num_rows_columns):
    matrix[r][r], matrix[num_rows_columns - 1 - r][r] = matrix[num_rows_columns - 1 - r][r], matrix[r][r]

for row in matrix:
    print(*row)


