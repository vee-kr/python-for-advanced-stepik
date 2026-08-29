
def chunked(text, num):
    cur_list = []
    ans = []
    k=0
    for elem in text:
        if k != num:
            cur_list.append(elem)
            k += 1
        elif k == num:
            k = 1
            ans.append(cur_list)
            cur_list = []
            cur_list.append(elem)
    ans.append(cur_list)
    print(ans)

text, num = input().split(), int(input())
chunked(text, num)






