num = list(input())

if len(num) <= 3:
    print(*num, sep='')
else:
    for i in range(len(num), 0, -3):
        num.insert(i, ',')
    del num[-1]

    print(*num, sep='')

