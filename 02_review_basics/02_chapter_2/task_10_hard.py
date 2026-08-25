num = int(input())
plug = "anton"
for i in range(1, num + 1):
    text = input()

    index = 0
    for char in text:
        if index < len(plug) and char == plug[index] :
            index += 1

    if index == len(plug):
        print(i, end=" ")
