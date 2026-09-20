word_lengths = [  len(set(input().lower())) for _ in range(int(input()))]
print(*word_lengths, sep="\n")