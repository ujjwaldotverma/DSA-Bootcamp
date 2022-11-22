import queue


#INBUILT QUEUE
q = queue.Queue()
q.put(1)                       #PUT = INSERT ELEMENT INTO QUEUE 
q.put(2)                       #GET = TAKE ELEMENT OUT OF QUEUE
q.put(3)
q.put(4)

while not q.empty():
    print(q.get())
    
    
#INBUILT STACK
import queue

q = queue.LifoQueue()
q.put(1)                       #PUT = INSERT ELEMENT INTO QUEUE 
q.put(2)                       #GET = TAKE ELEMENT OUT OF QUEUE
q.put(3)
q.put(4)

while not q.empty():
    print(q.get())
