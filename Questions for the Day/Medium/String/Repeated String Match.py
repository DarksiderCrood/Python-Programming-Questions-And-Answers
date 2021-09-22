'''
Given two strings A and B, find the minimum number of times A has to be
repeated such that B becomes a substring of the repeated A. If B cannot be a substring 
of A no matter how many times it is repeated, return -1.

Example 1:

Input: A = "abcd", B = "cdabcdab"
Output: 3
Explanation: After repeating A three times, 
we get "abcdabcdabcd".
Example 2:

Input: A = "aa", B = "a"
Output: 1
Explanation: B is already a substring of A.
Your Task:  
You don't need to read input or print anything. Complete the function repeatedStringMatch() 
which takes strings A and B as input parameters and returns the minimum number of operations 
to complete the task. If it is not possible then return -1.

Expected Time Complexity: O(|A| * |B|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |A|, |B| ≤ 103
'''

from itertools import combinations


# Find Subs of A
def A_Subs(A):
    subs = []
    for x in range(0, len(A)+1):
        temp = [list(x) for x in combinations(A, x)]
        if len(temp) > 0:
            subs.extend(temp)
    return subs


# Main
if __name__ == '__main__':
    # Inputs
    A = "abcd"
    B = "cdabcdab"

    count = 1
    while True:
        if B in A:
            print(count)
            break
        else:
            count+=1
            # result = A_Subs(A)
            A = A+A
