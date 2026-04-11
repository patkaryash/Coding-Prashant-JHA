class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    
    def inserttNode(rootNode, nodeValue):
        if rootNode.data == None:
            rootNode.data = nodeValue
        elif rootNode.data > nodeValue:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.rightChild, nodeValue)
                
                
    
                
                
                
                
                
                
                
                
          