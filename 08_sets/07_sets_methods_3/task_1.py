num_1, num_2 = set([int(x) for x in input()]), set([int(x) for x in input()])
if (num_1.isdisjoint(num_2)):
    print("NO")
else:
    print("YES")