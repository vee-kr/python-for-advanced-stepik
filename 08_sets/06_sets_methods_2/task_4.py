num = int(input())

set_1 = set(input())
for _ in range(num - 1):
    set_2 = set(input())
    set_1 &= set_2
print(*sorted(set_1))
