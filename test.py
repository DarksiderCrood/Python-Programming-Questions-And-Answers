A = [2,4,6,8,10,12,14,16,18,20]
D = 3

A.extend(A[:D])
del(A[:D])
print(A)