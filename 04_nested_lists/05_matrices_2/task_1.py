rows, columns = int(input()), int(input())
mult = []
for _ in range(rows):
    row = [0 for _ in range(columns)]
    mult.append(row)

for r in range(rows):
    for c in range(columns):
        mult[r][c] = r * c
        print(str(mult[r][c]).ljust(3), end=' ')
    print()
