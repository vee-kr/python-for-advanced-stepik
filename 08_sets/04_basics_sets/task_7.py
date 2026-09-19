num_1, num_2 = input(), input()
num_3 = num_1 + num_2
if len(set(num_3)) == 10:
    print("YES")
else: print("NO")