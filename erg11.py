from collections import Counter

file = input("Enter file name: ")

f = open(file, "r", encoding="utf8")
text = f.read()

keys=[]

while (len(text) != 1):
    if ((text[0]+text[1])=="{\"" or (text[0]+text[1])==",\"" or (text[0]+text[1])=="{\'" or (text[0]+text[1])=="{'"):
        x = text.find(":")
        y = text[:x]
        text = text[x:]
        keys.append(y[2:-1])
    else:
        text = text[1:]

ct = Counter(keys)
ct = ct.most_common(1)
count = 0
mostFrequentKey = ""

for i in str(ct):
    if i == "'":
        count += 1
    if count % 2 == 1:
        mostFrequentKey += i
mostFrequentKey = mostFrequentKey[1:]

if mostFrequentKey != "":
    print("Most frequent key is " + mostFrequentKey)
else:
    print("Wrong Input")
