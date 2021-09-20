

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
dc = {x:ar.count(x) for x in ar}
print(dc)
count = 0
for x,y in dc.items():
    if y%2!=0:
        mod = y-1
        count+=mod
    else:
        count+=y
print(int(count/2))