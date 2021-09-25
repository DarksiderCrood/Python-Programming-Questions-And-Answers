'''
Given an array having both positive and negative integers. 
The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
    N = 8
    A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
    Explanation: The largest subarray with
    sum 0 will be -2 2 -8 1 7.
'''

from itertools import combinations


A = [15, -2, 0, -8, 3, 7, 10, 23]

sub = []
sunze = []
for x in range(0, len(A)+1):
    temp = [list(i) for i in combinations(A, x)]
    if len(temp)>0:
        sub.extend(temp)
sunze = [g for g in sub if sum(g)==0]

# If output is largest sub array length with sum 0
maxz = max([len(k) for k in sunze])
print(maxz)

# If output is largest sub array with sum 0
temp = 0
for j in sunze:
    if len(j) > temp:
        c = j
        temp = len(j)
print(c)

