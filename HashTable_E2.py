#%%
import re 
word_tmp = []
word_dict = {}
with open("poem.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        tmp = re.findall("\w+",line)
        for t in tmp:
            if t not in word_dict.keys():
                word_dict[t] = 1 
            else:
                word_dict[t] += 1 
word_dict

#%%
class LinearProbing:
    def __init__(self):
        self.MAX = 10 
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        i = h 
        while self.arr[i]:
            if self.arr[i][0][0] == key:
                self.arr[i][0] = (key,value)
                return 
            i = (i+1) % self.MAX
            if i == h:
                raise Exception("Hash table full! Consider increasing table size.")
        self.arr[i] = (key,value)
        
    def __getitem__(self,key):
        h = self.get_hash(key)
        i = h 
        while self.arr[i]:
            if self.arr[i][0][0] == key:
                return self.arr[i][0][1]
            i = (i+1) % self.MAX
        raise KeyError("Key not Found.")
            

    def __delitem__(self,key):
        h = self.get_hash(key)
        i = h 
        while self.arr[i]:
            if self.arr[i][0][0] == key:
                del self.arr[i][0]
                return 
            i = (i+1)% self.MAX
        raise KeyError("Key not Found")

#%%
a = LinearProbing()
a["march 6"] = 1
a["march 3"] = 2
a["march 3"] = 3
a["march 17"] = 1
a["march 27"] = 2
a["march 5"] = 3
a["march 6"] = 3
a["march 7"] = 3
a["march 8"] = 3
a["march 9"] = 3

a["march 10"] = 3
# a["march 11"] = 3
# a["march 12"] = 3
# del a["march 27"]
a.arr



# %%
