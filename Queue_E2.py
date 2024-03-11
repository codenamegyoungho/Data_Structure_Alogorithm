#%%
from collections import deque 
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
        
    def front(self):
        return self.buffer[-1]

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty.")
            return 
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0 
    
    def size(self):
        return len(self.buffer)

#%%
def print_binary(n):
    queue = Queue()
    queue.enqueue("1")
    for i in range(n):
        front = queue.front()
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")
        print(queue.dequeue()) 

if __name__ == "__main__":
    print_binary(10)
