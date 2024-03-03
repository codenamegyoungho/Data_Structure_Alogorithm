#%%
### Node 만들어주는 class 생성
class Node():
    def __init__(self,input_data=None,next_data=None):
        self.data = input_data 
        self.next = next_data 



#%%
### Linked list 만들어주는 class 생성 
class LinkedList():
    def __init__(self):
        self.head = None
        
    
    def insert_at_beginning(self,data):
        node = Node(input_data=data,
                    next_data=self.head)
        
        self.head = node 
        print(f"self.head.data:{self.head.data},self.head.next:{self.head.next}")
        
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

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,self,None)
            return 
        itr = self.head 
        while itr.next:
            itr = itr.next 
        itr.next = Node(data,None)
    
    def insert_values(self,data,index):
        itr = self.head
        while index > 0:
            index -= 1 
            itr = itr.next 
        if itr and itr.next is not None:
            node = Node(data,itr.next)
            itr.next = node 
    
    def get_length(self):
        count = 0 
        itr = self.head 
        while itr:
            count += 1 
            itr = itr.next 
        return count 

    def remove_at(self,index):
        itr = self.head 
        while index >1:
            index -= 1 
            itr = itr.next 
        itr.next = itr.next.next



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_end(89)
    ll.insert_values(5555,1)
    ll.get_length()
    ll.remove_at(2)
    ll.print()

# %%
