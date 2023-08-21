num = int(input())
list = []
for i in range(num):
    userInput = input()
    list.append(userInput)

noSpace = [item.split(' ') for item in list]
#noColon = [item.split(';') for item in list]
listFlat = [item for l in noSpace for item in l]
print(listFlat)



if listFlat[0] == "int":
    print(1)
else:
    print(2)
count = 0
for element in listFlat:
        if element == '=':
            count += 1
        if element == '-':
            count += 1
        if element == '+':
            count += 1
        if element == '<':
            count += 1
        if element == '>':
            count += 1
        if element == '<<':
            count += 1
        if element in ['cin>>x;', 'cin>>y;']:
            count += 1

print("T(n) = " + str(count))