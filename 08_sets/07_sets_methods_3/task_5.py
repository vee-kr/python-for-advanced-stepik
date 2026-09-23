physics_1 = set([int(x) for x in input().split()])
physics_2 = set([int(x) for x in input().split()])
physics_3 = set([int(x) for x in input().split()])

only_3 = physics_3.difference(physics_1).difference(physics_2)
print(*sorted(only_3, reverse=True))