'''
Stack Basic Functions:
    1.Follows LIFO
    2.Push
    3.Pop
    4.Top 
    5.isEmpty
    6.Size
'''
#USING LIST
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self,item):
        self.__data.append(item)
        
    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        self.__data.pop()
        return pop.data
        
    def top(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        return self.__data[len(self.__data) - 1]
        
    def size(self):
        return len(self.__data)
        
    def isEmpty(self):
        return self.size() == 0

#USING LINKED LIST
class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0
        
    def push(self,item):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count +1 
        
    def pop(self):
        if self.isEmpty() is True:
            print("Empty Stack")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1 
        return data
        
    def top(self):
        if self.isEmpty() is True:
            print("Empty Stack")
            return
        data = self.__head.data
        return data
        
    def size(self):
        return self.__count
        
    def isEmpty(self):
        return self.size() == 0
