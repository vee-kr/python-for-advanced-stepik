num_rows_columns = int(input())
matrix = [[0 for _ in range(num_rows_columns)] for _ in range(num_rows_columns)]

for r in range(num_rows_columns):
    matrix[r][r] = 1
    matrix[r][num_rows_columns - 1 - r] = 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=' ')
    print()
