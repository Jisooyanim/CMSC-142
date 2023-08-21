def same_letters(stringA, stringB):
    count = 0
    res = []
    for char in stringA:
        if char in stringB:
            res.append(char)
    res =  list(set(res)) 
    for element in res:
        count += 1
    return count

print(same_letters('hello', 'world'))
print(same_letters('count', 'letters'))
print(same_letters('function', 'recurs'))
print(same_letters('string', 'double'))