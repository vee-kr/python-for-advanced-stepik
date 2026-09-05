num_rows_columns = int(input())
matrix = []
is_magic = "NO"

for _ in range(num_rows_columns):
    row = [int(i) for i in input().split()]
    matrix.append(row)

all_numbers = []
rows = []
columns = []
diagonal = []
reverse_diagonal = []

for r in range(num_rows_columns):
    rows.append(sum(matrix[r]))
    diagonal.append(matrix[r][r])
    reverse_diagonal.append(matrix[r][num_rows_columns - 1 - r])

column = []
for r in range(num_rows_columns):
    for c in range(num_rows_columns):
        if matrix[r][c] not in all_numbers and 1 <= matrix[r][c] <= (num_rows_columns ** 2):
            all_numbers.append(matrix[r][c])

        column.append(matrix[c][r])
    columns.append(sum(column))
    column.clear()

for i in range(num_rows_columns):
    if rows[i] == columns[i] == sum(diagonal) == sum(reverse_diagonal) and len(all_numbers) == (num_rows_columns ** 2):
       is_magic = "YES"
    else:
        is_magic = "NO"
        break

print(is_magic)


