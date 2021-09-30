import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    # Code Here
    dc = {x:ar.count(x) for x in ar}
    count = 0
    for x,y in dc.items():
        if y%2!=0:
            mod = y-1
            count+=mod
        else:
            count+=y
    return int(count/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()


# Raw Code 
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
dc = {x:ar.count(x) for x in ar}
print(dc)
count = 0
for x,y in dc.items():
    if y%2!=0:
        mod = y-1
        count+=mod
    else:
        count+=y
print(count/2)
print(int(count/2))