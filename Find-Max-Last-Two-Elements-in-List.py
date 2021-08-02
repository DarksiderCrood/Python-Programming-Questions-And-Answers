def max2(lst):
    largest = None
    sec_largest = []
    for x in lst:
        if not largest or x > largest:
            largest = x
    lst.remove(largest)
    sec_largest =  lst
    return largest, sec_largest


inp = '98 23 45 67 89 12 1'
l = inp.split(' ')
l2 = []
for x in l:
    l2.append(int(x))

r1, r2 = max2(l2)
r3, r4 = max2(r2)
print(r1,r3)