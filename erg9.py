import math

def split(word):
    return [char for char in word]

file = input("Enter file name: ")
f = open(file, "r", encoding="utf8")

cont = f.read()
chars = split(cont)
str_length = 0

lst = [""] * len(chars)
for i in range(0, len(chars)):
    if ord(chars[i]) % 2 == 1:
        lst[i] = ord(chars[i])
    else:
        lst[i] = ""
lst = list(filter(None, lst))

lf = [0] * 26
for i in range(0, len(lst)):
    for j in range(0, 26):
        if lst[i] == j + 65 or lst[i] == j + 97:
            lf[j] += 1
            str_length += 1

cont = cont.replace(" ", "")
cont = cont.replace("\n", "")

if str_length == 0:
    print("No letters with odd ASCII values")
else:
    for i in range(0, 26, 2):
        letter = chr(i + 65)
        print (letter + ": " + "*" * math.ceil((lf[i]/str_length)*100))

f.close()
