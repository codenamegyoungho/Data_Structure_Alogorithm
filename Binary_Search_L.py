#%%
def binary_search(numbers_list,number_to_find):
    left_index = 0 
    right_index = len(numbers_list) - 1 
    mid_index = 0 

    while left_index <= right_index:
        mid_index = (left_index+right_index) // 2 
        mid_number = numbers_list[mid_index] 

        if mid_number == number_to_find:
            return mid_index 
        
        if mid_number < number_to_find: 
            left_index = mid_index + 1 
        else:
            right_index = mid_index - 1
        
    return -1 
    
def binary_search_recursive(numbers_list,number_to_find,left_idx,right_idx):
    if right_idx < left_idx:
        return -1 
    mid_idx = (left_idx + right_idx) // 2 
    if mid_idx >= len(numbers_list) or mid_idx < 0:
        return -1 
    mid_number = numbers_list[mid_idx] 
    if mid_number == number_to_find:
        return mid_idx 
    if mid_number < number_to_find:
        left_idx = mid_idx + 1 
    else:
        right_idx = mid_idx - 1 
    return binary_search_recursive(numbers_list,number_to_find,left_idx,right_idx)

#%%
if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 15

    index = binary_search_recursive(numbers_list,number_to_find,0,len(numbers_list))
    print(index)
#%%
