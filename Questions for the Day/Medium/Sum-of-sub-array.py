from itertools import combinations

l = [1,4,3,5]
n = len(l)
sub = []

for i in range(0, n+1):
    temp = [list(x) for x in combinations(l, i)]
    if len(temp)>0:
        sub.extend(temp)
print(max(sum(x) for x in sub if len(x)!=n)) # not including sublist consisting all original list elements
