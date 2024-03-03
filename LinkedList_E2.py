#%%
### This class make nodes ++ prev,next,data 

class Node():
    def __init__(self,input_data:None,next_data:None,prev_data:None):
        self.data = input_data 
        self.next = next_data 
        self.prev = prev_data 

    
#%%
### This class make Linked List 
class DoublyLinkedList():
    def __init__(self):
        self.head = None 
    
    def insert_at_beginning(self,input_data):
        if self.head is None:
            node = Node(input_data=input_data,
                        next_data=self.head,
                        prev_data=None)
            self.head = node 
        else:
            node = Node(input_data=input_data,
                        next_data = self.head,
                        prev_data=None)
            self.head.prev = node 
            self.head = node 
        
    def insert_at_end(self,input_data):
        if self.head is None:
            node = Node(input_data=input_data,
                        next_data = None,
                        prev_data=None) 
            self.head = node  
        
        else:
            itr = self.head 
            while itr.next:
                itr = itr.next 
            node = Node(input_data=input_data,
                        next_data=None,
                        prev_data=itr)
            itr.next = node 
    
        
    def print_forward(self):
        if self.head is None:
            print("Linked List is empty.")
            return 
        itr = self.head
        llstr = "" 
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next 
        print(f"Linked list forward : {llstr}") 
    
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty.")
            return 
        
        itr = self.head 
        while itr.next:
            itr = itr.next
        llstr = ""
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.prev 
        print(f"Linked list reverse : {llstr}") 

    def get_length(self):
        count = 0 
        itr = self.head 
        while itr:
            count += 1 
            itr = itr.next 
        return count 
    
    def insert_at(self,index,input_data):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(input_data=input_data)
            return 
        count = 0 
        itr = self.head 
        while itr:
            if count == index -1:
                node = Node(input_data,itr.next,itr)
                if node.next:
                    node.next.prev = node 
                itr.next = node 
                break
            itr = itr.next 
            count +=1 
    
    def remove_at(self,index):
        if index <0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0 :
            self.head = self.head.next 
            self.head.prev = None 
            return 
        itr = self.head 
        count = 0 
        while itr:
            if count == index:
                itr.prev.next = itr.next 
                if itr.next:
                    itr.next.prev = itr.prev 
                break
            itr = itr.next 
            count += 1
     
    def insert_values(self,data_list):
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)


ll = DoublyLinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_beginning(3)
ll.insert_at(1,33)
ll.remove_at(2)
ll.insert_values([1,2,3])
ll.print_backward()
ll.print_forward()
ll.get_length()

# %%
