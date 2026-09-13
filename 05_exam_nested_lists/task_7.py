matrix = [['.' for _ in range(8)] for _ in range(8)]
position = input()
letters = 'abcdefgh'
position_dig = 8 - int(position[-1])
position_let = letters.index(position[0])
for r in range(8):
    for c in range(8):
        matrix[position_dig][position_let] = 'Q'
        x, y = position_let, position_dig

        if c == position_let:
            matrix[r][c] = '*'
        if r == position_dig:
            matrix[r][c] = '*'

        if abs(position_dig - r) == abs(position_let - c):
            matrix[r][c] = '*'


for row in matrix:
    print(*row)