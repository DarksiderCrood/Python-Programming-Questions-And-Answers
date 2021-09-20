

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
count = 0
while sorted(ar):
    b=ar.pop(0)
    a=ar.pop(0)
    if a==b:
        print([a,b])
        count+=1
    else:
        print([a,b])
print(count)