#%%
class BinarySearchTree:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

    def add_child(self,data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data) 
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    def search(self,val):
        if self.data == val:
            return True 
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False 
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False 



    def in_order_traversal(self):
        elements = []
        if self.left:
            elements +=self.left.in_order_traversal()
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        return elements 
#%%
b = BinarySearchTree(1)
b.add_child(2)
b.add_child(3)

