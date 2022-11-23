import queue
class BTnode:                                   #constructor
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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
    
def takeLevelWiseInput():
    
    q = queue.Queue()
    print("enter root.")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BTnode(rootData)
    q.put(root)
    
    while not(q.empty()):                                         
        curr_node = q.get()                                                 
        print("enter left child of, ",curr_node.data)                       #FOR LEFT SIDE INPUT
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BTnode(leftChildData)
            curr_node.left = leftChild
            q.put(leftChild)
            
        print("enter right child of, ",curr_node.data)                      #FOR RIGHT SIDE INPUT
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BTnode(rightChildData)
            curr_node.right = rightChild
            q.put(rightChild)
            
    return root
    
root = takeLevelWiseInput()
printTreeDetailed(root)
