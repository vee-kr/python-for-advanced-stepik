rows, columns = [int(x) for x in input().split()]

matrix = [[0 for _ in range(columns)] for _ in range(rows)]

counter = 1

for d in range(rows + columns - 1):
    for r in range(rows):
        for c in range(columns):
            if r + c == d:
                matrix[r][c] = counter
                counter += 1
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=" ")
    print()


