import re as regex

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> None:
        return self.data

class Tree:
    def __init__(self) -> None:
        self.nodes = []
    
    def newNode(self, operator:str) -> None:
        generateNode = Node(operator)
        nodeOne = self.nodes.pop()
        nodeTwo = self.nodes.pop()
        generateNode.right = nodeOne
        generateNode.left = nodeTwo
        self.nodes.append(generateNode)

def operatorPrecedence(operator:str) -> int:
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    if operator == '^':
        return 3
    else:
        return 0

def tokenizer(expression:str) -> list:
    tokens = []
    temp = regex.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", expression)
    i = 0

    while i < len(temp):
        if temp[i] in ['+', '-']:
            if temp[i + 1].isdigit() and (not temp [i - 1].isdigit()):
                tokens.append(temp[i] + temp[i + 1])
                i += 1
            else:
                tokens.append(temp[i])
        else:
            tokens.append(temp[i])
        i += 1
    return tokens

def createTree(tree:Tree, tokens:list):
    operators = ['+', '-', '*', '/', '^']
    stack = []

    for i in tokens:
        if i == '(':
            stack.append(i)
        
        if i.lstrip('-+').isdigit():
            generateNode = Node(i)
            tree.nodes.append(generateNode)
        
        if i in operators:
            while(len(stack) != 0 and stack[-1] != '(' and ((i == '^' and operatorPrecedence(i) < operatorPrecedence(stack[-1])) or (i != '^' and operatorPrecedence(i) <= operatorPrecedence(stack[-1])))):
                tree.newNode(stack.pop())
            stack.append(i)
        
        if i == ')':
            while(len(stack) != 0 and stack[-1] != '('):
                tree.newNode(stack.pop())
            stack.pop()
        
    for j in stack:
        tree.newNode(j)
    return tree.nodes[-1]

def preorder(root:Node) -> None:
    if root != None:
        print(str(root.data) + " ", end = "")
        preorder(root.left)
        preorder(root.right)

def postorder(root:Node) -> None:
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data) + " ", end = "")

def postorderStack(root:Node, stack:list) -> list:
    if root != None:
        postorderStack(root.left, stack)
        postorderStack(root.right, stack)
        stack.append(root.data)
    return stack

def evaluate(root):
    result = []
    stack = postorderStack(root, [])

    for i in stack:
        if i.lstrip('-+').isdigit():
            result.append(i)
        else:
            operandTwo = str(result.pop())
            operandOne = str(result.pop())
            operator = str(i)
            temp = eval(operandOne + operator + operandTwo)
            result.append(temp)
    return result[0]

def main():
    userInput = input("Enter expression: ")
    tokens = tokenizer(userInput)
    binaryTree = Tree()
    root = createTree(binaryTree, tokens)
    preorder(root)
    print("")
    postorder(root)
    res = evaluate(root)
    print("")
    print(res)

if __name__ == '__main__':
    main()