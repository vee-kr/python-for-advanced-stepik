text = input().split()
ans = []
cur_list = [text[0]]
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        cur_list.append(text[i])
    else:
        ans.append(cur_list)
        cur_list = [text[i]]
    if i == len(text) - 1:
        ans.append(cur_list)




print(ans)

