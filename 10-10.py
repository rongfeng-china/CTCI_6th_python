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

    def rankFromStream(self,root,value,count):
        if root  == None:
            return count
          
        if root.info == value:
            return count                    
        count = self.rankFromStream(root.left,value,count)
        count += 1
        count = self.rankFromStream(root.right,value,count)
        return count
     
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

value = 5
result =  tree.rankFromStream(tree.root,value,0)-1
print result

