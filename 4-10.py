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

def height(root):
    if root.left is None and root.right is None:
        return 0
    elif root.left is None:
        return height(root.right)+1
    elif root.right is None:
        return height(root.left)+1
    else:
        return max(height(root.left),height(root.right)+1)

def matchTree(r1,r2):
    if( r1 is None and r2 is not None) or (r1 is not None and r2 is None):
        return False
    if r1.info != r2.info:
        return False
    v1,v2 = True,True
    if not (r1.left is None and r2.left is None):
        v1 = matchTree(r1.left,r2.left)
    if not (r1.right is  None and r2.right is None):
        v2 = matchTree(r1.right,r2.right)
    return (v1 and v2)

def contrainsTree(root1,root2):
    if root1 is None:
        return False
    if root1.info != root2.info:
        if root1.left is not None:
            v1 = contrainsTree(root1.left,root2)
            if v1:
                return True
        if root1.right is not None:
            v2 = contrainsTree(root1.right,root2)
            if v2:
                return True
    else:
        v =  matchTree(root1,root2) 
        #print (v)
        if v == True:
            return True
        else:
            if root1.left is not None:
                v1 = contrainsTree(root1.left,root2)
                if v1 == True:
                    return True
            if root1.right is not None:
                print(root1.right)
                print(root2)
                v2 = contrainsTree(root1.right,root2)
                if v2 == True:
                    return True
                                                                  
#######test##########
#####   7
####  3    8
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
#######test##########
###    5
##    4 6
#####################
tree2 = BinarySearchTree()
tree2.create(5)
tree2.create(4)
tree2.create(6)
result = contrainsTree(tree.root,tree2.root)
print (result)
#print height(tree.root)
