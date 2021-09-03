from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

arr = [1,2,3,4,5] 
print(sub_lists(arr))

# or

l = [1,2,3]
s = []
for x in range(len(l)+1):
    for y in range(x+1,len(l)+1):
        r = l[x:y]
        s.append(r)
print(s)