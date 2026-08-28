num = int(input())
answer_list = list()
for _ in range(num):
    current_list = [i for i in range(1, num + 1)]
    answer_list.append(current_list)
print(*answer_list, sep='\n')