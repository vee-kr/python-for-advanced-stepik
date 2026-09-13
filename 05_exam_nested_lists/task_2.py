num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]
answer = []
for r in range(num):
    for c in range(num):
        if c >= num - 1 - r:
            answer.append(matrix[r][c])
print(max(answer))