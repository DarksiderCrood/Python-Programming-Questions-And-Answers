'''
Given a positive integer N, print count of set bits in it. 

Example 1:

Input:
    N = 6
Output:
    2
Explanation:
    Binary representation is '110' 
    So the count of the set bit is 2.
Example 2:

Input:
    8
Output:
    1
Explanation:
    Binary representation is '1000' 
    So the count of the set bit is 1.
'''


class Solution:
    def setBits(self, N):
        binary_num = bin(N).replace('0b', '')
        count = 0
        for x in str(binary_num):
            if int(x) == 1:
                count += 1
        return count


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.setBits(n)
        print(ans)