num_rows_columns = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num_rows_columns)]

counter = 1
for r in range(num_rows_columns):
    if counter <= num_rows_columns//2:
        counter += 1
        matrix[r], matrix[-(r+1)] = matrix[-(r+1)], matrix[r]


for row in matrix:
    print(*row)