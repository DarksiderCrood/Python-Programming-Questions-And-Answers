'''
Given an array of size n and a number k, find all elements that appear more than n/k times
Given an array of size n, find all elements in array that appear more than n/k times. 

For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, 
    then the output should be [2, 3]. Note that size of array is 8 (or n = 8), 
    so we need to find all elements that appear more than 2 (or 8/4) times. 
There are two elements that appear more than two times, 2 and 3. 
'''
from collections import Counter


arr = [3, 1, 4, 2, 2, 1, 2, 3, 3, 4, 4,2]
n = len(arr)
k = 4
div = n/k
Dict = Counter(arr)
lst = []

for keys,values in Dict.items():
    if values > div:
        lst.append(keys)
print(lst)
