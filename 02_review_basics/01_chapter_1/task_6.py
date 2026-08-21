num = input()
if len(num) == 5:
    print(num[::-1].lstrip('0'))
else:
    print((num[0] + num[:0:-1]).lstrip('0'))
    # print(int(num[0] + num[1:][::-1]))
