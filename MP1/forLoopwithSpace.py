num = int(input())
list = []
for i in range(num):
    userInput = input()
    list.append(userInput)

noSpace = [item.split(' ') for item in list]
#noColon = [item.split(';') for item in list]
listFlat = [item for l in noSpace for item in l]
#print(listFlat)

countConstant = 0 
countN = 0
outsideLoop = [] #elements not part of the loop
#Get the elements not part of the loop
for element in range(len(listFlat)):
    if listFlat[element] != '{':
        outsideLoop.append(listFlat[element])
    if listFlat[element] == '{':
        node = listFlat.index(listFlat[element])
        break
#print(outsideLoop)
#Get elemennts inside the loop
insideLoop = listFlat[node+1:]
#print(insideLoop)
#Checks if the higher limit is n or integer
if outsideLoop[len(outsideLoop) - 1] == 'i++)' and '*' not in outsideLoop:
    countN += 1
    if "n;" in outsideLoop:
        for element in range(len(outsideLoop)):
            if outsideLoop[element] == '=':
                countConstant += 1
                lowerLimit = outsideLoop[element + 1]
                lowerLimit = lowerLimit.split(';')
                lowerLimit = [i for i in lowerLimit if i]
                lowerLimit = [int(x) for x in lowerLimit]
                lowerLimit = [str(integer) for integer in lowerLimit] 
                lowerLimitString = "".join(lowerLimit)
                lowerLimitInt = int(lowerLimitString) #Integer only
                #print(lowerLimitInt)    
            if outsideLoop[element] == '<=':
                countConstant += 1
                countN += 1
        for element in insideLoop:
            if element == '=':
                countN += 1
            if element == '+':
                countN += 1
            if element == '*':
                countN += 1
            if element == '+=':
                countN += 1
            if element == '*=':
                countN += 1
            if element == 'a--;':
                countN += 1
        #print(countN)
        #print(countConstant)
        if -lowerLimitInt + 1 == 0:
            print("T(n) = " + str(countN) + "N + " + str(countConstant))
        else:
            multiply = -lowerLimitInt + 1
            #print(multiply)
            countConstant = (multiply * countN) + countConstant
            print("T(n) = " + str(countN) + "N - " + str(abs(countConstant)))
    else:
        for element in range(len(outsideLoop)):
            if outsideLoop[element] == '=':
                countConstant += 1
                lowerLimit = outsideLoop[element + 1]
                lowerLimit = lowerLimit.split(';')
                lowerLimit = [i for i in lowerLimit if i]
                lowerLimit = [int(x) for x in lowerLimit]
                lowerLimit = [str(integer) for integer in lowerLimit] 
                lowerLimitString = "".join(lowerLimit)
                lowerLimitInt = int(lowerLimitString) #Integer only
                #print(lowerLimitInt)
            if outsideLoop[element] == '<=':
                countConstant += 1
                countN += 1
                highLimit = outsideLoop[element + 1]
                highLimit = highLimit.split(';')
                highLimit = [i for i in highLimit if i] #Rid of space
                highLimit = [int(x) for x in highLimit] #Integer List
                highLimit = [str(integer) for integer in highLimit] 
                highLimitString = "".join(highLimit)
                highLimitInt = int(highLimitString) #Integer only
                #print(highLimitInt)
        
        for element in insideLoop:
            if element == '=':
                countN += 1
            if element == '*':
                countN += 1
            if element == '+=':
                countN += 1
            if element == 'a--;':
                countN += 1
        sigma = highLimitInt - lowerLimitInt + 1
        #print(countConstant)
        #print(countN)
        #print(sigma)
        countConstant = (countN * sigma) + countConstant
        print("T(n) = " + str(countConstant))
if '*=' in outsideLoop:
    countN += 1
    for element in range(len(outsideLoop)):
        if outsideLoop[element] == '=':
            countConstant += 1
            lowerLimit = outsideLoop[element + 1]
            lowerLimit = lowerLimit.split(';')
            lowerLimit = [i for i in lowerLimit if i]
            lowerLimit = [int(x) for x in lowerLimit]
            lowerLimit = [str(integer) for integer in lowerLimit] 
            lowerLimitString = "".join(lowerLimit)
            lowerLimitInt = int(lowerLimitString) #Integer only
            #print(lowerLimitInt) 
        if outsideLoop[element] == '<=':
            countConstant += 1
            countN += 1
        if outsideLoop[element] == '*=':
            base = outsideLoop[element + 1]# base)
    
    for element in insideLoop:
        if element == '=':
            countN += 1
        if element == '+':
            countN += 1
        if element == '*':
            countN += 1
        if element == '+=':
            countN += 1
        if element == '*=':
            countN += 1
        if element == 'a--;':
            countN += 1
    if -lowerLimitInt + 1 == 0:
        print("T(n) = " + str(countN) + " log(" + base + " n + " + str(countConstant))
    else:
        sigma = -lowerLimitInt + 1
        multiply = countN * sigma
        countConstant = multiply + countConstant
        print("T(n) = " + str(countN) + " log(" + base + " n - " + str(abs(countConstant)))
if '+=' in outsideLoop:
    countN += 1
    for element in range(len(outsideLoop)):
        if outsideLoop[element] == '=':
            countConstant += 1
            lowerLimit = outsideLoop[element + 1]
            lowerLimit = lowerLimit.split(';')
            lowerLimit = [i for i in lowerLimit if i]
            lowerLimit = [int(x) for x in lowerLimit]
            lowerLimit = [str(integer) for integer in lowerLimit] 
            lowerLimitString = "".join(lowerLimit)
            lowerLimitInt = int(lowerLimitString) #Integer only
            #print(lowerLimitInt) 
        if outsideLoop[element] == '<=':
            countConstant += 1
            countN += 1
        if outsideLoop[element] == '+=':
            base = outsideLoop[element + 1]
            base= base.split(')')
            base = [i for i in base if i]
            base = [int(x) for x in base]
            base = [str(integer) for integer in base] 
            baseString = "".join(base)
            baseInt = int(baseString)

    for element in insideLoop:
        if element == '=':
            countN += 1
        if element == '+':
            countN += 1
        if element == '*':
            countN += 1
        if element == '+=':
            countN += 1
        if element == '*=':
            countN += 1
        if element == 'a--;':
            countN += 1
        if element == 'b--;':
            countN += 1
    
    if -lowerLimitInt + 1 == 0:
        print("T(n) = " + str(countN) + "n/" + str(baseInt) + " + " + str(countConstant))
    else:
        sigma = -lowerLimitInt + 1
        multiply = countN * sigma 
        countConstant = multiply + countConstant
        print("T(n) = " + str(countN) + "n/" + str(baseInt) + " - " + str(abs(countConstant)))
if 'i--)' in outsideLoop:
    for element in range(len(outsideLoop)):
        if outsideLoop[element] == '=':
            countConstant += 1
            lowerLimit = outsideLoop[element + 1]
            lowerLimit = lowerLimit.split(';')
            lowerLimit = [i for i in lowerLimit if i]
            lowerLimitString = "".join(lowerLimit)


            if lowerLimitString == 'n':
                for element in range(len(outsideLoop)):
                    if outsideLoop[element] == '<=':
                        countConstant += 1
                print("T(n) = " + str(countConstant))
                break
            
        if outsideLoop[element] == '<=':
            highLimit = outsideLoop[element + 1]
            if highLimit == 'n;':
                print("infinite")
if '/=' in outsideLoop:
    for element in range(len(outsideLoop)):
        if outsideLoop[element] == '=':
            countConstant += 1

        if outsideLoop[element] == '<=':
            countConstant += 1
            countN += 1
            highLimit = outsideLoop[element + 1]
            highLimit = highLimit.split(';')
            highLimit = [i for i in highLimit if i] #Rid of space
            highLimit = [int(x) for x in highLimit] #Integer List
            highLimit = [str(integer) for integer in highLimit] 
            highLimitString = "".join(highLimit)
            highLimitInt = int(highLimitString)
            
            if type(highLimitInt) == int:
                print("T(n) = " + str(countConstant))
if '*' in outsideLoop :
    countI = 1
    for element in range(len(outsideLoop)):
        if outsideLoop[element] == '=':
            countConstant += 1
        if outsideLoop[element] == '*':
            countI += 1
            countConstant += 1
            countN += 1
        if outsideLoop[element] == '<=':
            countConstant += 1
            countN += 1
        if outsideLoop[element] == 'i++)':
            countN += 1
    
    for element in insideLoop:
        if element == '=':
            countN += 1
        if element == '+':
            countN += 1
        if element == '*':
            countN += 1
        if element == '+=':
            countN += 1
        if element == '*=':
            countN += 1
        if element == 'a--;':
            countN += 1
        if element == 'b--;':
            countN += 1
    
    if countI == 2:
        print("T(n) = " + str(countN) + " sqrt(n) + " + str(countConstant))
    else:
        print("T(n) = " + str(countN) + " cubert(n) + " + str(countConstant))