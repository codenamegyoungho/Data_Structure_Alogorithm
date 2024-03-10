#%%
from collections import deque 
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

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
import time 
import threading 

food_order_queue = Queue()
def producer(data):
    for order in data:
        food_order_queue.enqueue(order)
        time.sleep(0.5)
    

def consumer():
    time.sleep(1)
    while food_order_queue.size() > 0:
        order = food_order_queue.dequeue()
        print("Now serving:",order)
        time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=producer,args=(orders,))
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()




# %%
