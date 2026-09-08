rows, columns = [int(x) for x in input().split()]
row = list(range(1, columns + 1))
matrix = []
char = columns
for r in range(rows):
    matrix.append(row)
    if r % 2 == 0:
        row = list(range(char + columns, char, -1 ))
        char = row[0]
    else:
        row = list(range(char + 1, char + columns + 1))
        char = row[-1]

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=' ')
    print()
