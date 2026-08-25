word = input()
sentence = word + " запретил букву "

alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]


for alp in alphabet:
    if alp in sentence:
        old = sentence + alp
        old = " ".join(old.split())
        print(old.strip())
        sentence = sentence.replace(alp, '')

