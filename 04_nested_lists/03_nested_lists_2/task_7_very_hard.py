text = input().split()

ans = [[]]

n = 0
for i in range(1, len(text) + 1):
    for k in range(0, len(text) - n):
        ans.append(text[k:k+i])
    n += 1


print(ans)

