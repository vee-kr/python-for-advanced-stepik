sentence = 'Dying for the right cause is the most human thing we can do.'
unique_words = {word.lower().strip(":,.!?();") for word in sentence.split()}
print(*sorted(unique_words))