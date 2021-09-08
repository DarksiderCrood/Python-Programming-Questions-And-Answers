l = [1,2,5,3,6,8,9,0,6,4,2,1,2,3,4,5,6,7,8,90,1,23,54,675,21,78,9,12,4,312,4,54,67,57,898,98,56,54,3]
print("Sorted List Before Distinct Values")
l.sort(reverse=False)
print(l)
def rever():
 for x in l:
   if l.count(x) != 1:
    l.remove(x)
    rever()
 return l
# print(l.count(x))
b = rever()
print("Distinct Values:")
print(b)
