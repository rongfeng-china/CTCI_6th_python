class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.info)

class Tree:
    def __init__(self):
        self.root = None

    def create(self,node,arr):
        print (arr)
        mid_index = int(len(arr)/2)
        mid = arr[mid_index]
        node  = Node(mid)
        if self.root == None:
            self.root = node
        if len(arr) == 1:
            return node
        left_arr = arr[0:mid_index]
        right_arr = arr[mid_index+1:]
                
        if len(left_arr) != 0:
            node.left = self.create(node.left,left_arr)
        if len(right_arr) != 0:
            node.right = self.create(node.right,right_arr)
        return node

    def print_node(self,node):
        print (node.info)
        if node.left is not None:
            self.print_node(node.left)
        if node.right is not None:
            self.print_node(node.right)

    def print_tree(self):
        self.print_node(self.root)


tree = Tree()
tree.create(tree.root,[1,2,3,4,5])
tree.print_tree()       

print('second tree')
tr2 = Tree()
tr2.root = Node(3)
tr2.root.left = Node(2)
tr2.root.left.left = Node(1)
tr2.root.right = Node(4)

tr2.print_tree()
