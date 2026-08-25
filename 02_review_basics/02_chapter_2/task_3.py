numbers = [int(i) for i in input().split()]
k = 0  # 1
for _ in range(len(numbers)//2):
    numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
    k = k + 2
print(*numbers)

for i in range(0, len(numbers)-1, 2):  # 2
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(*numbers)
