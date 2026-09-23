biology_1 = set([int(x) for x in input().split()])
biology_2 = set([int(x) for x in input().split()])
biology_3 = set([int(x) for x in input().split()])

all_scores = set([i for i in range(1, 11)])
dont_appear = all_scores.difference(biology_1).difference(biology_2).difference(biology_3)
print(*sorted(dont_appear))
