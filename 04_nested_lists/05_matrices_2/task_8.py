chessboard = [['.' for _ in range(8)] for _ in range(8)]

position = []
alph = 'abcdefgh'
for elem in input():
    position.append(elem)

row = 8-int(position[-1])
column = alph.index(position[0])

chessboard[row][column] = 'N'
x, y = column, row


x_moves = [x - 1, x - 1, x + 1, x + 1, x + 2, x + 2, x - 2, x - 2]
y_moves = [y - 2, y + 2, y - 2, y + 2, y - 1, y + 1, y - 1, y + 1]
c = 0
for _ in range(8):
    y_p = y_moves[c]
    x_p = x_moves[c]
    c += 1
    if 0 <=  x_p <= 7 and 0 <= y_p <= 7:
        chessboard[y_p][x_p] = '*'
    else:
        continue


for r in chessboard:
    print(*r)









