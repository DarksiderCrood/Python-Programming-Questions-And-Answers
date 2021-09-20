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
