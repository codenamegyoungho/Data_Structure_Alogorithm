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
def reverse_string(input_data,):
    stack = Stack()
    for element in input_data:
        stack.push(element)

    rstr = ""
    while stack.size() != 0:
        rstr += stack.pop()
    return rstr 

if __name__ == "__main__":
    print(reverse_string("hello world"))

#%%
def is_balanced(input_data):
    stack = Stack()
    for element in input_data:
        stack.push(element)
    return stack 
a = is_balanced("{(a+b)}")
a.pop()






# %%
