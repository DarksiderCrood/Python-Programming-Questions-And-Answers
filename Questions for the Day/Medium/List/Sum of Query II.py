'''
You are given an array arr[] of n integers and q queries in an array queries[] of length 2*q containing l, r pair for all q queries. You need to compute the following sum over q queries.

 

Array is 1-Indexed.

Example 1:

Input: n = 4
arr = {1, 2, 3, 4}
q = 2
queries = {1, 4, 2, 3}
Output: 10 5
Explaination: In the first query we need sum 
from 1 to 4 which is 1+2+3+4 = 10. In the 
second query we need sum from 2 to 3 which is 
2 + 3 = 5.
Your Task:
You do not need to read input or print anything. 
Your task is to complete the function querySum() which takes n, arr, q 
and queries as input parameters and returns the answer for all the queries.

Expected Time Complexity: O(n+q)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n, q ≤ 1000
1 ≤ arri ≤ 106
1 ≤ l ≤ r ≤ n
'''


class Solution:
    def querySum(self, n, arr, q, queries):
        my_pairs = list()
        out = []
        while(queries):
            a = queries.pop(0); b = queries.pop(0)
            my_pairs.append([a,b])
        
        for x in my_pairs:
            out.append(sum(arr[x[0]-1:x[1]]))
        return out


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0,2*q,2):
            queries[i] = int(queries[i])
            queries[i+1] = int(queries[i+1])
        
        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in(ans):
            print(it,end=" ")
        print()


# Raw Work
n = 4
arr = [1, 2, 3, 4]
q = 2
queries = [1, 4, 2, 3]
my_pairs = list()
while(queries):
    a = queries.pop(0); b = queries.pop(0)
    my_pairs.append([a,b])

for x in my_pairs:
    print(sum(arr[x[0]-1:x[1]]), end=" ")