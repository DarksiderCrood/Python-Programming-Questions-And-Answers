'''
You are given an array A of integers of length N. You need to calculate factorial of each number. 
The answer can be very large, so print it modulo 109 + 7.
 

Example 1:

Input:
N = 5
A[] = {0, 1, 2, 3, 4}
Output:
1 1 2 6 24
Explanation:
Factorial of 0 is 1, 
factorial of 1 is 1, factorial of 2 is 2, 
factorial of 3 is 6 and so on.

Example 2:

Input:
N = 3
A[] = {5, 6, 3}
Output:
120 720 6
Explanation:
Factorial of 5 is 120, 
factorial of 6 is 720, 
factorial of 3 is 6.

Your Task:
Complete the function factorial() which takes list a and single integer n, 
as input parameters and returns a list of factorials of the numbers in the list a.


Expected Time Complexity: O(max(A) + N)
Expected Auxiliary Space: O(max(A))


Constraints:
1 <= N <= 105
0 <= A[i] <= 105
'''

class Solution:
    def factorial(self,a, n):
        l = []
        for x in a:
            if x == 0:
                l.append(1)
            else:
                s = 1
                for y in range(1,x+1):
                    s*=y
                l.append(s)
        return l


if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        a=list(map(int , input().strip().split()))
        ob = Solution()
        res = ob.factorial(a, n)
        for i in res:
            print(i,end=" ")
        print()
        tc=tc-1