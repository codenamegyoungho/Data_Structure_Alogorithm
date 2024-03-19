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
    
    def find_minimum(self):
        current_node = self 
        min = current_node.data 
        while current_node.left:
            current_node = current_node.left
            min = current_node.data 
        return min  
            
    def find_maximum(self):
        current_node = self 
        max = current_node.data 
        while current_node.right:
            current_node = current_node.right
            max = current_node.data 
        return max  
    
    def calculate_sum(self):
        elements = self.in_order_traversal()
        sum_ele = sum(elements)
        return sum_ele
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements 
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements.extend(self.left.pre_order_traversal()) 
        if self.right:
            elements.extend(self.right.pre_order_traversal())
        return elements
    
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

#%%
elements = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
# numbers_tree.in_order_traversal()
# numbers_tree.find_minimum()
# numbers_tree.find_maximum()
# numbers_tree.calculate_sum()
numbers_tree.pre_order_traversal()
