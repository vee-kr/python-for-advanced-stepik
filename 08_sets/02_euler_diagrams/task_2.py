n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
only_1_and_2 = n + m - t - x
only_2_and_3 = m + k - t - y
only_1_and_3 = n + k - t - z

print ((n - only_1_and_3 - t - only_1_and_2) + (m - t - only_1_and_2 - only_2_and_3) + (k - t - only_1_and_3 - only_2_and_3))  # only 1 book
print(only_1_and_3 + only_1_and_2 + only_2_and_3)  # only 2 books
print(a - (k + only_1_and_2 + (m - only_1_and_2 - only_2_and_3 - t) + (n - only_1_and_2 - t - only_1_and_3)))  # 0 books