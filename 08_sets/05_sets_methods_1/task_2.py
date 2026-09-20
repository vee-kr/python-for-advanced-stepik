ans = ""  # 1
for _ in range(int(input())):
    ans += input().lower()

print(len(set(ans)))

symbols = set()  # 2
for _ in range(int(input())):
    for char in input().lower():
        symbols.add(char)
print(len(symbols))