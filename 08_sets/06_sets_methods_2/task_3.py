set_1, set_2 = set([int(x) for x in input().split()]), set([int(x) for x in input().split()])
set_3 = set_1 - set_2
print(*sorted(set_3))