class Node:
    #create a node in the tree
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        #insert root node in if there is no root node
        if self.root == None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)
    
    def insertNode(self, rootNode, value):
        if value < rootNode.data:
            #inserting node in the left and right position 
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left,  value)  #recursive call
        else:
                if rootNode.right is None:
                    rootNode.right = Node(value)  #70
                else: 
                    self.insertNode(rootNode.left, value)
            
btObj = BinaryTree()
btObj.insert(50)
btObj.insert(30) 
btObj.insert(70)

print(btObj)
 
            
class BSTNode:
     def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None       