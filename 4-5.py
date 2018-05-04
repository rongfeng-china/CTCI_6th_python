class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def isBinarySearchTree(node):
    if node.left is None and node.right is None:
        return True
    elif node.left is None:
        if isBinarySearchTree(node.right) and node.info <= minimum(node.right):
            return True
        else:
            return False
    elif node.right is None:
        if isBinarySearchTree(node.left) and node.info >= maximum(node.left):
            return True
        else:
            return False
    else:
        if isBinarySearchTree(node.left) and isBinarySearchTree(node.right) and node.info <= minimum(node.right) and node.info >= maximum(node.left):
            return True
        else:
            return False

def maximum(node):
    if node.right is None:
        return node.info
    else:
        return minimum(node.right)

def minimum(node):
    if node.left is None:
        return node.info
    else:
        return minimum(node.left)

def height(root):
    if root.left is None and root.right is None:
        return 0
    elif root.left is None:
        return height(root.right)+1
    elif root.right is None:
        return height(root.left)+1
    else:
        return max(height(root.left),height(root.right)+1)

tree = BinarySearchTree()
tree.create(7)
tree.create(3)
tree.create(5)
tree.create(2)
tree.create(1)
tree.create(4)
tree.create(6)
tree.create(7)

print (isBinarySearchTree(tree.root))


tree2 = Node(3)
tree2.left = Node(5)
tree2.right = Node(8)
print (isBinarySearchTree(tree2))
