rows, columns = [int(x) for x in input().split()]

matrix = []

row = list(range(1, columns + 1))

for _ in range(rows):  # 1
    for elem in row:
        print(str(elem).ljust(3), end=' ')
    print()
    row.append(row.pop(0))

for _ in range(rows):  # 2
    matrix.append(row)
    row = row[1:] + row[:1]

for r in matrix:
    print(*r)


