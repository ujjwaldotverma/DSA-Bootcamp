'''
Queue Basic Functions:
    1.Follows FIFO
    2.Enqueue()         #insert at rear end
    3.Dequeue()         #deletion of front element
    4.Size()
    5.isEmpty()
    6.Front()            #first element of queue
'''
#USING ARRAY
class QueueUsingArray:
    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0
    
    def enqueue(self,data):
        self.__arr.append(data)
        self.__count += 1
            
    def dequeue(self):
        if self.__count == 0:
            return -1
        
        element = self.__arr[self.__front]
        self.__front += 1
        self.__count -= 1
        return element
        
    def size(self):
        return self.__count
            
    def front(self):
        if self.__count == 0:
            return -1
        return self.__arr[self.__front]
        
    def isEmpty(self):
        return self.size() == 0
    
        
q = QueueUsingArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
while q.isEmpty() is False:
    print(q.front())
    q.dequeue()

print(q.dequeue())

#USING LINKED LIST 
class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None
class QueueUsingLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = None
        
    def enqueue(self,element):
        newNode = Node(element)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        
        self.__tail = newNode
        self.__count = self.__count + 1
        
        
    def dequeue(self):
        if self.__head is None:
            print("Empty Queue")
            return
        else:
            data = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1 
            return data
        
    def isEmpty(self):
        return self.size() == 0
        
    def size(self):
        return self.__count
        
    def front(self):
        if self.__head is None:
            print("Empty Queue")
            return
        else:
            data = self.__head.data
            return data
            
q = QueueUsingLL()
q.enqueue(1)  
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)

while q.isEmpty is False:
    print(q.dequeue())
    
q.front()
