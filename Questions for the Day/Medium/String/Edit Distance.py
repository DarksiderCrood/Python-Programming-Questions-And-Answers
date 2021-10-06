s = list("geeks")
t = list("gesek")

if s == t:
    print(0)
else:
    count = 0
    for x,y in zip(s,t):
        if x==y:
            continue
        elif y not in s:
            count+=1
            inx = s.index(x)
            s.insert(inx+1,y)
        elif x not in t:
            count+=1
            s.remove(x)
            

s = ''.join(s)
t = ''.join(t)
print(s,t)
print(count)


