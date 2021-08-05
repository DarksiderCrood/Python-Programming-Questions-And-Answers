def sub_lists(arr): 
    sub_list = [[]]  # Store all the sublists 

    for i in range(len(arr) + 1):        
        for j in range(i + 1, len(arr) + 1): 
            sub = arr[i:j] 
            sub_list.append(sub)  
    return sub_list 
  
arr = [4,5,8,4,8,5,2,58,486] 
print(sub_lists(arr))