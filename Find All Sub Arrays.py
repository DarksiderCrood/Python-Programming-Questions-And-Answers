lst = [1,2,3]
size = len(lst)
item = 0

result = [sublist for sublist in 
        (lst[x:x+size] for x in range(len(lst) - size + 1))
        if item not in sublist
    ]

print(result)