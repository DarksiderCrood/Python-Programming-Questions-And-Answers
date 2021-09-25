from itertools import combinations


A = [15, -2, 0, -8, 3, 7, 10, 23]
sub = []

for x in range(0, len(A)+1):
    temp = [list(i) for i in combinations(A, x)]
    if len(temp)>0:
        sub.extend(temp)
print(sub)