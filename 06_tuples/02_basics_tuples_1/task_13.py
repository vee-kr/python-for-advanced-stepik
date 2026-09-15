for i in range(len(tuples)):
    array = list(tuples[i])
    array[-1] = 100
    tuples[i] = tuple(array)

print(tuples)

new_arr = [elem[:-1] + (100,) for elem in tuples]
print(new_arr)
