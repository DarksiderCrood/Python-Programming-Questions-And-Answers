arr = [15,-2,2,-8,1,7,10,23]
n = len(arr)



if n == 0:
    print(0)
maxl = 0    
hashdic = {}
maxlcopy = 0
for i in range(n):
    if maxlcopy + arr[i] == 0:
        maxl = i + 1
        maxlcopy += arr[i]
    
    elif maxlcopy+arr[i] in hashdic:
        maxl = max(maxl,i - hashdic[maxlcopy+arr[i]])
        maxlcopy += arr[i]
    else:
        hashdic[maxlcopy + arr[i]] = i
        maxlcopy += arr[i]
            
print(maxl)