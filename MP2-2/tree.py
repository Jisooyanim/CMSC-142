class Tree:
    def __init__(self, name, parent = None):
        self.children = list()
        self.parent = parent
        self.name = name
    
    def delete(self, node):
        node.parent.children.remove(node)
        node.parent = None
        node.children = None
        node = None

class directoryNode(Tree):
    def __init__(self, name, parent = None):
        super().__init__(name,parent)
    
    def insert(self, child:Tree):
        self.children.append(child)
    
    def remove(self, node):
        node.parent.children.remove(node)
        node.parent = None
        node.children = None
        node = None
    
    def search(self, name):
        for child in self.children:
            if child.name == name:
                return child
            res = child.search(name)
            if res:
                return res
        return None

class fileNode(Tree):
    def __init__(self, name, parent = None):
        super().__init__(name, parent)
        self.data = bytearray()
    
    def append(self, contents):
        self.data.extend(bytes(contents, 'utf-8'))
        self.data.extend(bytes('\n', 'utf-8'))