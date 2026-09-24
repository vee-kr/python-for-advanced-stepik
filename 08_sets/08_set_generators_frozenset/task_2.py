words = ['summer', 'city', 'Earth', 'peace', 'kindness', 'Dog', 'turtle']
first_letters = {elem[0].lower() for elem in words}
print(*sorted(first_letters))
