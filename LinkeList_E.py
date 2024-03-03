#%% 
### This class purpose is making Node. 
class Node():
    def __init__(self,input_data=None,next_data=None):
        self.data = input_data
        self.next = next_data 

# %%
### This class purpose is making linked list. 
class LinkedList():
    def __init__(self):
        self.head = None 
    
    def insert_at_beginning(self,input_data):
        node = Node(input_data=input_data,
                    next_data=self.head)
        self.head = node 
        
    def insert_at_end(self,input_data):
        if self.head is None:
            self.head = Node(input_data,None)
            return
        
        itr = self.head 
        while itr.next:
            itr = itr.next 
        itr.next = Node(input_data,None)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return 
        itr = self.head 
        llstr = ""
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next 
        print(llstr)

    def get_length(self):
        count = 0 
        itr = self.head 
        while itr:
            itr = itr.next 
            count += 1 
        return count

    def insert_values(self,data_list):
        itr = self.head 
        while itr.next:
            itr = itr.next    
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self,index,input_data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
    
        if index == 0:
            self.insert_at_beginning(input_data)
            return 
        itr = self.head
        count = 0 
        while itr:
            if count == index-1:
                itr.next = Node(input_data,itr.next)
                break
            itr = itr.next
            count += 1   

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next 
            return 
        count = 0 
        itr = self.head 
        while itr:
            if count == index - 1:
                itr.next = itr.next.next 
                break 
            itr = itr.next 
            count += 1 

    def insert_after_value(self,data_after,data_to_insert):
        Find = False 
        itr = self.head 
        while itr:
            if itr.data == data_after: 
                Find = True 
                break 
            itr = itr.next 
        if not Find:
            raise Exception("Couldn't find the data_after")
        if itr.next:
            itr.next = Node(data_to_insert,itr.next)
            return 
        else:
            itr.next = Node(data_to_insert,None)
            return 
    
    def remove_by_value(self,wish_data):
        if self.head == None:
            return 
        if self.head.data ==wish_data:
            self.head = self.head.next 
            return 
        itr = self.head 
        while itr.next:
            if itr.next.data == wish_data:
                itr.next = itr.next.next 
                break 
            itr = itr.next 
        

        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(55)
    ll.insert_at(index=1,input_data=66)
    # ll.remove_at(1)
    # ll.insert_after_value(6,88)
    ll.remove_by_value(4)
    ll.print()
    ll.get_length()

# %%





