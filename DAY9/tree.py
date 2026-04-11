class Tree:
    def __init__(self,value):     #constructor
        self.value = value         #instance variable
        self.children = []         #instance variable
    
    def addChild(self,child):          #method
        self.children.append(child)       

    def __str__(self,level=0):        #method
        ret = "  " * level + str(self.value) + "\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret


rootNode=Tree("N1")
N2 = Tree("N2") 
N3 = Tree("N3") 
N4 = Tree("N4") 
N5 = Tree("N5") 
N6 = Tree("N6") 
N7 = Tree("N7") 
N9 = Tree("N9") 
N10 = Tree("N10") 
rootNode.addChild(N2)
rootNode.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N6)
N3.addChild(N7)
N4.addChild(N9)
N4.addChild(N10)
#creating root node
# hot = Tree("Hot")
# cold = Tree("Cold")                    
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# nonAlcoholic = Tree("Non-Alcoholic")     
# Alcoholic = Tree("Alcoholic")

# #add child nodes in tree
# rootNode.addChild(hot)
# rootNode.addChild(cold)

# hot.addChild(tea)
# hot.addChild(coffee)

# cold.addChild(nonAlcoholic)
# cold.addChild(Alcoholic)

print(rootNode)