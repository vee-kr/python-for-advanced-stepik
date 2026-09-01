num_rows_columns = int(input())
matrix = []
for _ in range(num_rows_columns):
    row = [int(x) for x in input().split()]
    matrix.append(row)

nums = []
for r in range(num_rows_columns):
    for c in range(num_rows_columns):
        if ( c <= r and r <= num_rows_columns - 1 - c) or ( c >= r and r >= num_rows_columns - 1 - c ):
            nums.append(matrix[r][c])

print(max(nums))