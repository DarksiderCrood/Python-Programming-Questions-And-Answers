num = 5

for x in range(1,num+1): # if want to add same number and 1 as a factor of num add '1,num+1' in range
    if num%x==0:
        print(x)