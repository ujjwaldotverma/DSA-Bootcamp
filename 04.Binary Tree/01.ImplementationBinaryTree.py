class BTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)
    
def printTreeDetailed(root):
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
    
btn1=BTnode(1)
btn2=BTnode(2)
btn3=BTnode(3)
btn4=BTnode(4)
btn5=BTnode(5)
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
printTreeDetailed(btn1)
