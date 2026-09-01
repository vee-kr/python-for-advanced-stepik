num_rows_columns = int(input())
matrix = []
for _ in range(num_rows_columns):
    rows = [int(i) for i in input().split()]
    matrix.append(rows)

nums = []
for r in range(num_rows_columns):
    for c in range(num_rows_columns):
        if c <= r:
            nums.append(matrix[r][c])

print(max(nums))

