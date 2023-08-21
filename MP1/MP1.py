outsideLoop = []
countConstant = 0
countN = 0

def getInput():
    num = int(input())
    list = []
    
    for i in range(num):
        userInput = input()
        list.append(userInput)
    
    noSpace = [item.split(' ') for item in list]
    listFlat = [item for l in noSpace for item in l]
    return listFlat

def noLoop(list):
    count = 0
    for element in list:
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

def countInside(insideLoop):
    global countN
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
        if element == '*=':
            countN += 1
        if element == 'a--;':
            countN += 1
        if element == 'b--;':
            countN += 1
    return countN

def forLoop1(list):
    global countConstant
    global countN
    
    for element in range(len(list)):
        if list[element] != 'i++){':
            outsideLoop.append(list[element])
        if list[element] == 'i++){':
            countN += 1
            node = list.index(list[element])  
    for element in outsideLoop:
        if element == 'i=0;':
            countConstant += 1
        if element == 'i<n;':
            countConstant += 1
            countN += 1
    insideLoop = list[node+1:]
    countInside(insideLoop)
    print("T(n) = " + str(countN) +"N + " + str(countConstant))

def getLimit(list, element):
    limit = list[element + 1]
    limit = limit.split(';')
    limit = [i for i in limit if i]
    limit = [int(x) for x in limit]
    limit = [str(integer) for integer in limit]
    limitString = "".join(limit)
    limitInt = int(limitString)
    return limitInt

def forLoop2(list):
    global countConstant
    global countN

    for element in range(len(list)):
        if list[element] != '{':
            outsideLoop.append(list[element])
        if list[element] == '{':
            node = list.index(list[element])
            break
    insideLoop = list[node+1:]

    if outsideLoop[len(outsideLoop) - 1] == 'i++)' and '*' not in outsideLoop:
        countN += 1
        if 'n;' in outsideLoop:
            for element in range(len(outsideLoop)):
                if outsideLoop[element] == '=':
                    countConstant += 1
                    lowerLimit = getLimit(outsideLoop, element)
                if outsideLoop[element] == '<=':
                    countConstant += 1
                    countN += 1
            countInside(insideLoop)
            if -lowerLimit + 1 == 0:
                print("T(n) = " + str(countN) + "N + " + str(countConstant))
                quit()
            else:
                multiply = -lowerLimit + 1
                countConstant = (multiply * countN) + countConstant
                print("T(n) = " + str(countN) + "N - " + str(abs(countConstant)))
                quit()
        else:
            for element in range(len(outsideLoop)):
                if outsideLoop[element] == '=':
                    countConstant += 1
                    lowerLimit = getLimit(outsideLoop, element)
                if outsideLoop[element] == '<=':
                    countConstant += 1
                    countN += 1
                    highLimit = getLimit(outsideLoop, element)
            countInside(insideLoop)
            sigma = highLimit - lowerLimit + 1
            countConstant = (countN * sigma) + countConstant
            print("T(n) = " + str(countConstant))
            quit()
    
    if '*=' in outsideLoop:
        countN += 1
        for element in range(len(outsideLoop)):
            if outsideLoop[element] == '=':
                countConstant += 1
                lowerLimit = getLimit(outsideLoop, element)
            if outsideLoop[element] == '<=':
                countConstant += 1
                countN += 1
            if outsideLoop[element] == '*=':
                base = outsideLoop[element + 1]
        countInside(insideLoop)
        if -lowerLimit + 1 == 0:
            print("T(n) = " + str(countN) + " log(" + base + " n + " + str(countConstant))
            quit()
        else:
            sigma = -lowerLimit + 1
            multiply = countN * sigma
            countConstant = multiply + countConstant
            print("T(n) = " + str(countN) + " log(" + base + " n - " + str(abs(countConstant)))
            quit()
    
    if '+=' in outsideLoop:
        countN += 1
        for element in range(len(outsideLoop)):
            if outsideLoop[element] == '=':
                countConstant += 1
                lowerLimit = getLimit(outsideLoop, element)
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
        countInside(insideLoop)
        if -lowerLimit + 1 == 0:
            print("T(n) = " + str(countN) + "n/" + str(baseInt) + " + " + str(countConstant))
            quit()
        else:
            sigma = -lowerLimit + 1
            multiply = countN * sigma
            countConstant = multiply + countConstant
            print("T(n) = " + str(countN) + "n/" + str(baseInt) + " - " + str(abs(countConstant)))
            quit()
    
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
                    quit()
                    break
            
            if outsideLoop[element] == '<=':
                highLimit = outsideLoop[element + 1]
                if highLimit == 'n;':
                    print("infinite")
                    quit()

    if '/=' in outsideLoop:
        for element in range(len(outsideLoop)):
            if outsideLoop[element] == '=':
                countConstant += 1

            if outsideLoop[element] == '<=':
                countConstant += 1
                countN += 1
                highLimit = getLimit(outsideLoop, element)
            
                if type(highLimit) == int:
                    print("T(n) = " + str(countConstant))
                    quit()

    if '*' in outsideLoop:
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
        countInside(insideLoop)
    
    if countI == 2:
        print("T(n) = " + str(countN) + " sqrt(n) + " + str(countConstant))
        quit()
    else:
        print("T(n) = " + str(countN) + " cubert(n) + " + str(countConstant))
        quit()
        
def main():
    userInput = getInput()

    if userInput[0] == 'int':
        noLoop(userInput)
    if userInput[0] == 'for(int':
        forLoop1(userInput)
    if userInput[0] == 'for':
        forLoop2(userInput)

if __name__ == '__main__':
    main()