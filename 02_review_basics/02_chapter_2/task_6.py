num = int(input())
numbers = [int(input()) for _ in range(num)]
target = int(input())
flag = "НЕТ"
for i in range(len(numbers)):
    for k in range(i + 1, len(numbers)):
        if numbers[i] * numbers[k] == target:
            flag = "ДА"
            break
    if flag == "ДА": break
print(flag)