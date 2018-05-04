class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
        self.parent = None

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
                        current.left.parent = current
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        current.right.parent = current
                        break
                else:
                    break

    def inorderSucc(self,node):
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        elif node == node.parent.right:
            while node == node.parent.right and node.parent != self.root:
                node = node.parent
            if node == self.root.right:
                return None
            return node.parent
        else:
            return node.parent


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
tree.create(8)


print (tree.inorderSucc(tree.root.left.left))
print (tree.inorderSucc(tree.root.left.right.right))
print (tree.inorderSucc(tree.root.right))
