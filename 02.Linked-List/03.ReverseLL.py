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

def reverseR(head):                       #fn to reverse LL Recursively
    if head is None or head.next is None: #TC = O(n)
        return head
        
    smallHead = reverseR(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

def reverseI(head):                       #fn to reverse LL Iteratively
    prev = None                           #TC = O(n)
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        head = prev
    return head
    
head = takeInput()
printLL(head)
head = reverseI(head)
printLL(head)
