'''
For an integer N find the number of trailing zeroes in N!.

Example 1:

Input:
N = 5
Output:
1
Explanation:
5! = 120 so the number of trailing zero is 1.
Example 2:

Input:
N = 4
Output:
0
Explanation:
4! = 24 so the number of trailing zero is 0.
Your Task:  
You don't need to read input or print anything. 
Your task is to complete the function trailingZeroes() which take an integer N 
as an input parameter and returns the count of trailing zeroes in the N!.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 109
'''
## Solution
# Take the length of the string value of what you're checking
# Trim off trailing zeros from a copy of the string
# Take the length again, of the trimmed string
# Subtract the new length from the old length to get the number of zeroes trailing.


class Solution:
    def trailingZeroes(self, N):
        y=1
        for x in range(1, N+1):
            y*=x
        return len(str(y)) - len(str(y).rstrip('0'))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)