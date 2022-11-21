class BTnode:                                   #constructor
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def printTree(root):                            #print the tree
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)
    
def printTreeDetailed(root):                    #print but better
    if root == None:
        return
    print(root.data, end = ':')
    if root.left != None:
        print("L",root.left.data, end = ',')
    if root.right != None:
        print("R",root.right.data, end = '')
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)
    
def treeInput():                            #ask user for input
    rootData = input()
    root = BT
    
btn1=BTnode(1)                                 #creating nodes
btn2=BTnode(2)
btn3=BTnode(3)
btn4=BTnode(4)
btn5=BTnode(5)
btn1.left=btn2                                  #connecting edges
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
printTreeDetailed(btn1)                         #function call
