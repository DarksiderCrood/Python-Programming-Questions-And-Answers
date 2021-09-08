'''
Geek created a random series and given a name geek-onacci series. 
Given four integers A, B, C, N. A, B, C represents the first three numbers of geek-onacci series. 
Find the Nth number of the series. 
The nth number of geek-onacci series is a sum of the last three numbers 
(summation of N-1th, N-2th, and N-3th geek-onacci numbers)

Input:
    1. The first line of the input contains a single integer T denoting the number of test cases. 
    The description of T test cases follows.
    2. The first line of each test case contains four space-separated integers A, B, C, and N.

Output: For each test case, print Nth geek-onacci number

Constraints:
    1. 1 <= T <= 3
    2. 1 <= A, B, C <= 100
    3. 4 <= N <= 10

Example:
Input:
    3
    1 3 2 4
    1 3 2 5
    1 3 2 6

Output:
    6
    11
    19
'''


class Solution:
    def GeekOnacci(self, lt):
        Nth_pos = lt[-1]
        lt.remove(lt[-1])
        series = []
        for x in range(0, Nth_pos):
            if x==0 or x==1 or x==2:
                series.append(lt[x])
            else:
                series.append(series[x-1]+series[x-2]+series[x-3])
        return series[-1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        l = list(''.join(input()).split(' '))
        lst = [int(x) for x in l]
        ob = Solution()
        print(ob.GeekOnacci(lst))
