'''
Given an integer N, count the numbers having an odd number of factors from 1 to N (inclusive).
 

Example 1:

Input:
    N = 5
Output:
    2
Explanation:
    From 1 - 5 only 2 numbers,
    1 and 4 are having odd number
    of factors.
'''


# Not Optimized One
'''class Solution:
    def count (self, N):
        count = 0
        fact = []
        for x in range(1, N+1):
            a = []
            for y in range(1, x+1): 
                if x%y==0:
                    a.append(y)
            fact.append(a)
        print(fact)
        for x in fact:
            if len(x)%2!=0:
                count+=1   
        return count'''

# Optimized One
class Solution:
    def count (self, N):
        count = 0
        for x in range(1, N+1):
            a = []
            for y in range(1, x+1): 
                if x%y==0:
                    a.append(y)
            if len(a)%2!=0:
                count+=1  
        return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))