from tree import (directoryNode, fileNode)
import getErrors
import fnmatch, re

class fileHandler:
    def __init__(self, root: directoryNode):
        self.root = root
        self.pwd = root
    
    def _pwd(self, node: directoryNode | fileNode = None):
        directories = list()
        cwd = self.pwd if node is None else node 
        
        while cwd != self.root:
            directories.insert(0, cwd.name)
            cwd = cwd.parent
        return '/' + '/'.join(directories)

    def _resolvePath(self, path:str):
        match path:
            case '/':
                return self.root
            case '.':
                return self.pwd
            case '..':
                return self.pwd.parent if self.pwd != self.root else self.root
            
        if path.startswith('/'):
            currentNode = self.root
        else:
            currentNode = self.pwd
        parts   = path.split('/')

        for part in parts:
            if not part:
                continue
                
            match part:
                case '..':
                    currentNode     = currentNode.parent if currentNode != self.root else self.root
                case '.':
                    continue
                case _:
                    found   = False
                    for child in currentNode.children:    
                        if child.name == part:
                            currentNode = child
                            found  = True
                            break
                    if not found:
                        return None
        return currentNode

    def _resolveParentandName(self, path:str):
        parts   = path.split('/')
        name    = parts[-1]
        if not name:
            return None, ''

        if len(parts) == 1:
            return self.pwd, name

        parentPath = '/'.join(parts[:-1])
        parent = self._resolvePath(parentPath)
        return parent, name
    
    def _wildcardHandler(self, paths:list):
        cPaths = list()

        for path in paths:
            if '*' in path:
                wildcards = re.findall(r'[^\\^/^\s]*\*[^\\^/^\s]*', path)
                wildcardSubstring = path.replace(wildcards[0], '')
                wildcardNode  = self._resolvePath(wildcardSubstring)
                if wildcardNode:
                    children = [wildcardSubstring + child.name for child in wildcardNode.children]
                    matches = fnmatch.filter(children, wildcardSubstring+wildcards[0])
                    for match in matches:
                        tmp     = path
                        cPaths.append(tmp.replace(wildcardSubstring+wildcards[0], match, 1))
            else:
                cPaths.append(path)
            
        cPaths   = list(dict.fromkeys(cPaths))
        wildcardBool   = False
        for cp in cPaths:
            wildcardBool   = '*' in cp
            if wildcardBool:
                cPaths   = self._wildcardHandler(cPaths)
                break
        return cPaths

    def mkdir(self, path):
        parent, name = self._resolveParentandName(path)
        
        if not parent:
            return 2, getErrors.errors['mkdir'][2].replace('{}', path)

        if any(child.name == name for child in parent.children):
            return 1, getErrors.errors['mkdir'][1].replace('{}', name)
        
        parent.insert(directoryNode(name, parent))
        return 0, getErrors.errors['mkdir'][0]
    
    def rmdir(self, path):
        node = self._resolvePath(path)

        if type(node) is fileNode:
            return 5, getErrors.errors['rmdir'][5].replace('{}', path)

        if node == self.root:
            return 4, getErrors.errors['rmdir'][4]

        if not node:
            return 2, getErrors.errors['rmdir'][2].replace('{}', path)

        if len(node.children) > 0:
            return 1, getErrors.errors['rmdir'][1].replace('{}', path)
        
        if node == self.pwd and self.pwd.parent is not None:
            self.pwd = self.pwd.parent
        self.pwd.remove(node)
        return 0, getErrors.errors['rmdir'][0]
    
    def cd(self, path):
        toPathNode = self._resolvePath(path)

        if not toPathNode:
            return 1, getErrors.errors['cd'][1].replace('{}', path)
        
        if type(toPathNode) is fileNode:
            return 2, getErrors.errors['cd'][2].replace('{}', path)
        
        self.pwd = toPathNode
        return 0, getErrors.errors['cd'][0]
    
    def ls(self, path):
        paths = self._wildcardHandler([path])
        cwds = [self._resolvePath(p) for p in paths]

        if len(cwds) == 1 and cwds[0] == None:
            return 1, getErrors.errors['ls'][1].replace('{}', path)
        results = dict()

        for cwd in cwds:
            if type(cwd) is directoryNode:
                results[self._pwd(cwd)] = list()
        
        for cwd in cwds:
            if type(cwd) is directoryNode:
                for child in cwd.children:
                    results[self._pwd(cwd)].append(child.name)
        return 0, results
    
    def mv(self, sources:list(), destination:str):
        errors = list()
        
        destinationNode = self._resolvePath(destination)
        if not destinationNode and len(sources) > 1:
            return 1, getErrors.errors['mv'][1].replace('{}', destination)
        
        for sourceWildcard in sources:
            sourcePaths = self._wildcardHandler([sourceWildcard])
            sourceNodes = [self._resolvePath(s) for s in sourcePaths]

            if len(sourcePaths) == 0 or not sourceNodes:
                errors.append((1, getErrors.errors['mv'][1].replace('{}', sourceWildcard)))
                continue
            
            if sourceWildcard == destination:
                errors.append((2, getErrors.errors['mv'][2].replace('{}', sourceWildcard)))
                continue
            
            if type(destinationNode) is fileNode:
                errors.append((3, getErrors.errors['mv'][3].replace('{destination}', destination).replace('{source}', sourceWildcard)))
                continue

            if destinationNode:
                for node in sourceNodes:
                    if not node:
                        errors.append((1, getErrors.errors['mv'][1].replace('{}', sourceWildcard)))
                        continue
                    node.parent.children.remove(node)
                    node.parent = destinationNode
                    node.parent.insert(node)
            else:
                if len(sourceNodes) > 1:
                    errors.append((1, getErrors.errors['mv'][1].replace('{}', destination)))
                    continue
                for node in sourceNodes:
                    destinationName = destination.split('/')[-1]     
                    parentPath = destination.replace(destinationName, '')  
                    parentNode = self._resolvePath(parentPath)   
                    node.parent.children.remove(node)
                    node.parent = parentNode
                    node.parent.insert(node)
                    node.name = destinationName
        return errors
    
    def cp(self, sources: list, destination:str):
        errors = list()
        destinationNode = self._resolvePath(destination)

        if not destinationNode and len(sources) > 1:
            return 1, getErrors.errors['cp'][1].replace('{}', destination)
        
        for sourceWildcard in sources:
            sourcePaths = self._wildcardHandler([sourceWildcard])
            sourceNodes = [self._resolvePath(s) for s in sourcePaths]

            if len(sourcePaths) == 0:
                errors.append((1, getErrors.errors['cp'][1].replace('{}', sourceWildcard)))
                continue

            if sourceWildcard == destination:
                errors.append((2, getErrors.errors['cp'][2].replace('{}', sourceWildcard)))
                continue

            if type(destinationNode) is directoryNode:
                for node in sourceNodes:
                    if not node:
                        errors.append((1, getErrors.errors['cp'][1].replace('{}', sourceWildcard)))
                        continue
                    destinationNode.insert(node)
            
            else:
                if len(sourceNodes) > 1:
                    errors.append((1, getErrors.errors['mv'][1].replace('{}', destination)))
                    continue
                for node in sourceNodes:
                    destinationName = destination.split('/')[-1]                    
                    parentPath = destination.replace(destinationName, '')     
                    parentNode = self._resolvePath(parentPath)               
                    node.parent = parentNode                                  
                    if type(node) is directoryNode:
                        newNode = directoryNode(node.name, node.parent)
                    if type(node) is fileNode:
                        newNode = fileNode(node.name, node.parent)
                    newNode.name = destination
                    node.parent.insert(newNode)   
        return errors
    
    def rm(self, sources:list):
        errors = list()

        for sourceWildcard in sources:
            sourcePaths = self._wildcardHandler([sourceWildcard])
            sourceNodes = [self._resolvePath(s) for s in sourcePaths]

            if len(sourcePaths) == 0 or not sourceNodes:
                errors.append((1, getErrors.errors['rm'][1].replace('{}', sourceWildcard)))
                continue
            
            for s in sourceNodes:
                s.parent.delete(s)
        return errors
    
    def edit(self, filename, data:str = None):
        node = self._resolvePath(filename)
        parent, name = self._resolveParentandName(filename)

        if isinstance(node, directoryNode):
            return 1, getErrors.errors['edit'][1].replace('{}', filename)

        if not node:
            if not parent:
                return 2, getErrors.errors['edit'][2].replace('{}', filename)
            parent.insert(fileNode(name, parent))
            return 0, getErrors.errors['edit'][0]
        
        if not data:
            return 3, getErrors.errors['edit'][3]
        node.append(data)
        return 0, getErrors.errors['edit'][0]
    
    def show(self, filename):
        node = self._resolvePath(filename)

        if not isinstance(node, fileNode):
            return 1, getErrors.errors['show'][1].replace('{}', filename)
        return 0, node.data
    
    def whereIs(self, name, path = '/'):
        stack = []
        directories = self.ls(path)

        for directory in directories:
            for file in directories[directory]:
                if re.match(name.replace('*', '.*'), file):
                    if path == '/':
                        stack.append(directory + file)
                    else:
                        stack.append(directory + '/' + file)
                
                try:
                    stack += self.whereIs(name, directory + '/' + file)
                except:
                    continue
        return stack