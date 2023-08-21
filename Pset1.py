def intReverse(n):
    rev = 0   # 1          
    
    while n > 0:  # n + 1         
        rev = (rev * 10) + (n % 10) # n + n + n + n
        n //= 10   # n + n
    return rev  # 1          
    #T(n) = 7n + 3
def strReverse(string):
    s = "" # 1
    for char in string: # n + 1
        s = char + s # n + n
    return s # 1
    #T(n) = 3n + 3
def sorted(A, n):
    stack = [None, None, None] # 1

    for i in range(n-1): # n + 1
        if(A[i] < A[i+1]): # n 
            stack[0] = "decreasing" # n
        elif(A[i] > A[i+1]): # n 
            stack[1] = "increasing" # n
        else: # n
            stack[2] = "equal" # n

    for element in stack: # n + 1
        if element == None: # 1
            stack.remove(element) # 2n

    if(len(stack) == 1 and stack[0] == "decreasing" or stack[0] == "increasing"): # 1 + 1 + 1 + 1 + 1 + 1 = 6
        return True # 1
    elif(len(stack) == 2 and 'equal' in stack):  # 1 + 1 + 1 = 3
        return False # 1
    else: 
        return False # 1
    #T(n) = 10n + 16
def remainder(a, b):
    if a < b: # 1
        return a
    return remainder(a - b, b) # 1 + 1
    #T(n) = 3n + 1

#print(intReverse(4321))
#print(strReverse("ecargard"))
#print(sorted([4, 4, 4, 4, 4], 5))
#print(remainder(9,2))