#%%
from typing import List
def bubble_sort(elements:List,key:str)->List:
    size = len(elements)
    for i in range(size-1):
        swapped = False 
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp 
                swapped = True 
        if not swapped:
            break 
    return elements 
#%% 
if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    answer = bubble_sort(elements,key="transaction_amount")
    print(answer)

#%%
dic = [{"name":1},{"name":2}]
dic[0]["name"]