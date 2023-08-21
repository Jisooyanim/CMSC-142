num = int(input())
list = []
for i in range(num):
    userInput = input()
    list.append(userInput)

noSpace = [item.split(' ') for item in list]
#noColon = [item.split(';') for item in list]
listFlat = [item for l in noSpace for item in l]
print(listFlat)

countConstant = 0 
countN = 0
outsideLoop = [] #elements not part of the loop
#Get the elements not part of the loop
for element in range(len(listFlat)):
    if listFlat[element] != 'i++){':
        outsideLoop.append(listFlat[element])
    if listFlat[element] == 'i++){':
        countN += 1
        node = listFlat.index(listFlat[element])
#Get T(n) of outsideLoop
for element in outsideLoop:
    if element == 'i=0;':
        countConstant += 1
    if element == 'i<n;':
        countConstant += 1
        countN += 1
#Get elements inside the loop
insideLoop = listFlat[node+1:]
for element in insideLoop:
    if element == '=':
        countN += 1
    if element == '+':
        countN += 1
    if element == '-':
        countN += 1
    if element == '*':
        countN += 1
    if element == '/':
        countN += 1
    if element == '-+':
        countN += 1
    if element == '+=':
        countN += 1

print(insideLoop)
#print(outsideLoop)
#print(node)
print("T(n) = " + str(countN) +"N + " + str(countConstant))