from nltk.tokenize import word_tokenize

num = int(input())
list = []
for i in range(num):
    userInput = input()
    list.append(userInput)

#print(list)
count = 0
rawright = 0
rawrleft = 0
token = [word_tokenize(i) for i in list]

for i in token:
    print(i)
    
for line in token:
    for element in line:
        if element == '=':
            count += 1
        if element == '-':
            count += 1
        if element == '+':
            count += 1
        if element == '<':
            rawrleft += 1
            count += 1
        if element == '>':
            rawright += 1
            count += 1

if rawright != 0 or rawrleft != 0:
    if rawright != 0:
        if rawright == 2:
            count -= 1
        elif rawright % 2 == 0:
            count -= rawright/2
    if rawrleft != 0:
        if rawrleft == 2:
            count -= 1
        elif rawrleft % 2 == 0:
            count -= rawrleft/2
    print(int(count))
else:
    print(count)