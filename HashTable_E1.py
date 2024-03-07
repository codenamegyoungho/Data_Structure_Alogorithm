#%%
import pandas as pd 
df = pd.read_csv("nyc_weather.csv")
avg_first = sum(df["temperature(F)"][0:7]) / 7 
max_ten = max(df["temperature(F)"][0:10]) 
max_ten
avg_first
df

#%% 
class HashTable:
    def __init__(self,data_len,):
        self.MAX = data_len 
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0 
        for element in key:
            h += ord(element) 
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        find = False 
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                find = True 
                break 
        if not find:
            self.arr[h].append((key,value))




    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

#%%
arr = []
t = HashTable(10)
for i in range(len(df)):
    arr.append((df.iloc[i][0],df.iloc[i][1]))
for kv in arr:
    t[kv[0]] = kv[1]
t.arr 
t["Jan 9"]
t["Jan 4"]
    



