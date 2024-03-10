#%%
from collections import deque 
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

#%%
def is_balanced(input_data):
    stack = Stack()
    correct = ["()","[]","{}"]
    for element in input_data:
        if element in "[{(":
            stack.push(element)
        elif element in "]})" and stack.size() > 0:
            if (stack.peek() + element) in correct:
                stack.pop()
                pass 
            else:
                print("wrong")
                break 
    if stack.size() != 0:
        print("params wrong ")
            
is_balanced("(a+b))")






# %%
a = deque("Hello")


