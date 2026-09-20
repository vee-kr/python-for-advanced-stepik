text = input().lower()  # 1
words = set()

for char in text:
    if char in ".,;:-?!": text = text.replace(char, "")

text = text.split()
for elem in text:
    words.add(elem)
print(len(words))

words = [elem.lower().strip(".,;:-?!") for elem in input().split()]  # 2
print(len(set(words)))






