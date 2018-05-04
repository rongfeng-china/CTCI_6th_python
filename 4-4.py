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

    def isBalanced(self,node):
        if node.left is None and node.right is None:
            return True
        elif node.left is None:
            if self.height(node) <= 1 and self.isBalanced(node.right):
                return True
            else:
                return False
        elif node.right is None:
            if  self.height(node) <= 1 and self.isBalanced(node.left):
                return True
            else:
                return False
        else:
            a = self.height(node.left)-self.height(node.right)
            if abs(a) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right):
                return True
            else:
                return False
             
    def height(self,root):
        if root.left is None and root.right is None:
            return 0
        elif root.left is None:
            return self.height(root.right)+1
        elif root.right is None:
            return self.height(root.left)+1
        else:
            return max(self.height(root.left),self.height(root.right)+1)

tree = BinarySearchTree()
tree.create(7)
tree.create(3)
tree.create(5)
tree.create(2)
tree.create(1)
tree.create(4)
tree.create(6)
tree.create(8)
print (tree.isBalanced(tree.root))

tree2 = BinarySearchTree()
tree2.create(4)
tree2.create(2)
tree2.create(1)
tree2.create(3)
tree2.create(6)
tree2.create(5)
print (tree2.isBalanced(tree2.root))
