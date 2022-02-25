"""

There are two kinds of bots A and B in a 1-D array. A bot can only move left 
while B can only move right. There are also empty spaces in between represented by #. 
But its also given that the bots cannot cross over each other.

Given the initial state and final state, we should tell if the transformation is possible.

NOTE: There can be many bots of the same type in a particular array. 


Example 1:

Input:
s1 = #B#A#
s2 = ##BA#
Output: Yes
Explanation: Because we can reach the 
final state by moving 'B' to the 
right one step.

Example 2:

Input:
s1 = #B#A#
s2 = #A#B# 
Output: No
Explanation: Because the robots 
cannot cross each other.


Your Task:  
You don't need to read input or print anything. 
Your task is to complete the function moveRobots() which takes the initial and 
final states as strings s1 and s2 respectively and returns if a valid transformation can be done. 
Return "Yes" if possible, else "No".

 

Expected Time Complexity: O(|s1|)
Expected Auxiliary Space: O(|s1|)

 

Constraints:
1 <= |s1| = |s2| <= 105
The strings only consists of 'A', 'B' and '#'.

"""



class Solution:
    def moveRobots (self, s1, s2):
        check1 = ''.join([x for x in s1 if x=='A' or x=='B'])
        if check1 == 'AB':
            return 'No'
        else:
            check2 = ''.join([x for x in s2 if x=='A' or x=='B'])
            if check2 == 'AB':
                return 'No'
            else:
                return 'Yes'


if __name__ == '__main__': 
    # t = int (input ())
    # for _ in range (t):
        # s1 = input()
        # s2 = input()
    s1 = '#B#A#'
    s2 = '#A#B#'

    ob = Solution()
    print(ob.moveRobots(s1, s2))
