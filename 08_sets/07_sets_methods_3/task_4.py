math_1, math_2, math_3 = set([int(x) for x in input().split()]), set([int(x) for x in input().split()]), set([int(x) for x in input().split()])

all_set = math_1.union(math_2).union(math_3)  # 1
intersection = all_set.intersection(math_1).intersection(math_2).intersection(math_3)
all_set = all_set.difference(intersection)
print(*sorted(all_set))

result = (math_1 | math_2 | math_3) - (math_1 & math_2 & math_3)  # 2

