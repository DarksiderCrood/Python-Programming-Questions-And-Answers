from itertools import combinations

l = [1,4,3]
n = len(l)
sub = []

for i in range(0, n+1):
    temp = [list(x) for x in combinations(l, i)]
    if len(temp)>0:
        sub.extend(temp)
print(sub)
maxs = [len(z) for z in sub]

print(max(sub))