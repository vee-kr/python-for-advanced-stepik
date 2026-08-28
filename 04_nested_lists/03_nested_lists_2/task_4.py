def pascal(num_line):

    line = [1]
    print(*line)
    for _ in range(num_line-1):
        line = [0] + line + [0]

        new_line = []
        for i in range(len(line) - 1):
            new_line.append(line[i] + line[i + 1])

        line = new_line

        print(*line)


num = int(input())

pascal(num)


