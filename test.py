#max from list without inbuild
l = [-1,-3,-4,-7,-2,-5,-7,-10,-5,-2]
max = l[0]
for i in l:
    if max < i:
        max = i
print(max)
