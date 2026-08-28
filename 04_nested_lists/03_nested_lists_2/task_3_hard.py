def pascal(num_line):

    line = [1]
    for _ in range(num_line):

        new_line = [1]
        for i in range(len(line) - 1):
            new_line.append(line[i] + line[i + 1])
        new_line.append(1)

        line = new_line

    return line


num = int(input())

print(pascal(num))


