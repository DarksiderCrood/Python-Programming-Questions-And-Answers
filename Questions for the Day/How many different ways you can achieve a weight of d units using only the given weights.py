'''
Question:
    Given two weights of a and b units, in how many different ways you can achieve a weight of d units using 
    only the given weights? Any of the given weights can be used any number of times (including 0 number of times).

Note: 
    Two ways are considered different if either the number of times a is used or number of times b is 
    used is different in the two ways.

Input Format:
    The first line of input consists of an integer 
    T denoting the number of test cases.
    Each test case consists of only one line containing three space separated integers a, b and d.

Output Format:
    For each test case, print the answer in a separate line.

Constraints:
    1 ≤T≤ 10^5
    1 ≤ a < b ≤ 10^9
    0≤d≤10^9

Sample Input 1
    4
    2 3 7
    4 10 6
    6 14 0
    2 3 6

Sample Output 1
    1
    0
    1
    2

Explanation
    Test case 1: 7 can only be achieved by using 2 two times and 3 one time.
    Test case 2: 6 can't be achieved by using 4 and 10 .So, 0 ways are there.
'''