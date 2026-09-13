num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]

flag = "YES"
for r in range(num):
    for c in range(num):
        if matrix[r][c] != matrix[num - 1 - c][num - 1 - r]:
            flag = "NO"
            break
print(flag)