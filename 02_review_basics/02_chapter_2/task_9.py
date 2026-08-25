text = input()

count = 0  # 1
tails = [0]
for i in range(len(text) - 1):
    if text[i] == "Р":
        if text[i + 1] == "Р":
            count += 1
        elif text[i + 1] == "О":
            count += 1
            tails.append(count)
            count = 0
        if text[i + 1] == "Р" and (i + 1) == len(text)-1:
            count += 1
            tails.append(count)
            break
    elif text[i] == "О" and (i + 1) == len(text)-1 and text[i + 1] == "Р":
        count += 1
        tails.append(count)
        break
print(max(tails))

tails = text.split('О')  # 2
print(len(max(tails)))




