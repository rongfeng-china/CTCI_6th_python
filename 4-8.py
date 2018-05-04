from LinkedList import *
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
        self.lists = []

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

    def createLevelLinkedList(self,node):
        if node.level >= len(self.lists):
            ll = LinkedList()
            self.lists.append(ll)
        self.lists[node.level].addNode(node.info)
        if node.left is None and node.right is None:
            return
        elif node.left is None:
            self.createLevelLinkedList(node.right)
        elif node.right is None:
            self.createLevelLinkedList(node.left)
        else:
            self.createLevelLinkedList(node.left)
            self.createLevelLinkedList(node.right)
    
    def print_ll(self,level):
        ll = self.lists[level]
        print (ll)

    #########################
    ### root level = 0
    #########################
    def level(self,node):
        if node == self.root:
            node.level = 0
        if node.left is not None:
            node.left.level = node.level+1
            self.level(node.left)
        if node.right is not None:
            node.right.level = node.level+1
            self.level(node.right)

    def commonAncestor(self,p,q):
        sub = p.level-q.level
        if sub >0:
            for i in range(sub):
                p = p.parent
        if sub <0:
            for i in range(-sub):
                q = q.parent
        while p.parent is not None and q.parent is not None and p != q:
            p = p.parent
            q = q.parent
        return p

#######test##########
#####   7
####  3   8
### 2   5
## 1   4 6
#####################
tree = BinarySearchTree()
tree.create(7)
tree.create(3)
tree.create(5)
tree.create(2)
tree.create(1)
tree.create(4)
tree.create(6)
tree.create(8)

tree.level(tree.root)

#print (tree.root.left.left)
ancestor = tree.commonAncestor(tree.root.left.left, tree.root.left.right.right)
ancestor2 = tree.commonAncestor(tree.root.right,tree.root.left.right.left)
print (ancestor)
print (ancestor2)
