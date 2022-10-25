class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):                      #fn to print LL
    while head is not None:
        print(str(head.data)+"->",end="")
        head = head.next
    print("None")
    return
def takeInput():                          #fn to input LL
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode                     
            tail = newNode
    return head
    
def length(head):                         #fn to find length of the LL
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insertAti(head,i,data):               #fn to input at i
    if i<0 or i>length(head):
        return head
        
    count = 0
    prev = None
    curr = head
    
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    newNode = Node(data)
    
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
    
    return head
    
head = takeInput()
printLL(head)
head = insertAti(head,2,9)
printLL(head)
