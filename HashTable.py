#%%
def get_hash(key):
    h = 0 
    for char in key:
        h += ord(char)
    return h  
#%%
### Make Hash Table class + Collision handling 
class HashTable:
    def __init__(self):
        self.MAX = 10 
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        # self.arr[h] = value 
        # self.arr[h].append((key,value))
        found = False 
        for idx,element in enumerate(self.arr[h]):
            if len(element) ==2 and element[0] == key:
                self.arr[h][idx] = (key,value) 
                found = True 
                break 
        if not found:
            self.arr[h].append((key,value))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for kv in (self.arr[h]):
            if kv[0] == key:
                return kv[1] 

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                print("del",idx)
                del self.arr[h][idx]

t = HashTable()
t["march 6"] = 1999
t["march 6"] = 2000
t["march 17"] = 1777
t.arr
t["march 17"]
del t["march 6"]
t.arr
