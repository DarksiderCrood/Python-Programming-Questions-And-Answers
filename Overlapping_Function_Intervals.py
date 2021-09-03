'''
Problem Statement:
    You have been given the start and end times of 'N' intervals. Write a function to check 
    if any two intervals overlap with each other.
Note :
    If an interval ends at time T and another interval starts at the same time, they are 
    not considered overlapping intervals.
Input Format :
    The first line contains an Integer 'T' which denotes the number of test cases or queries to be run. 
    Then the test cases follow.

The first line of each test case or query contains an integer 'N' representing the total number of intervals.
The second line contains 'N' single space-separated integers representing the starting time of the intervals. 
The third line contains 'N' single space-separated integers representing the end time of the intervals.

Output Format :
    For each test case, return true if overlapping intervals are present. Otherwise, return false.

Output for every test case will be printed in a separate line.
Note :
    You do not have to print anything. Just return the boolean value.
Constraints :
    1 <= T <= 10^2
    0 <= N <= 10^5
    0 <= Start[i] <= 10^15
    1 <= End[i] <= 10^15  

Time Limit: 
    1 sec

Sample Input 1 :
    1
    3
    1 2 3
    2 3 4
Sample Output 1 :
    false
Explanation For Sample Input 1:
    Here, in given intervals [1, 2], [2, 3], [3, 4], there are no overlapping intervals present.

Sample Input 2 :
    2
    1
    100
    200
    2
    2 1
    3 4
Sample Output 2 :
    false
    true
'''

# Method 1
# def check(final,n):
#     if(n==1):
#         return "false"
#     for i in range(1,n):
#         if(final[i][0]<final[i-1][1]):
#             return "true"
#     return "false"


# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(0,t):
#         n = int(input())
#         range1 = list(map(int,input().split()))
#         range2 = list(map(int,input().split()))
#         final = []
#         for i in range(0,n):
#             final.append((range1[i],range2[i]))
#         final.sort()
#         ans = check(final,n)
#         print(ans)


# Method 2
'''   
    Time Complexity = O(N ^ 2)
    Space Complexity = O(1)
    
    where N is the number of intervals given
'''


from sys import stdin,setrecursionlimit
setrecursionlimit(10**7) # Used to set the maximum depth of the Python interpreter stack to the required limit. 
                         # This limit prevents any program from getting into infinite recursion, 
                         # Otherwise infinite recursion will lead to overflow of the C stack and crash the Python.


# If end of on internval is less than equal to starting of other internval then there is no overlap.
def sureForOverlap( start1, end1, start2, end2) :
    if (end1 <= start2 or end2 <= start1) :
        return False
    return True


# Check all posible combinations.
def checkForOverlappingIntervals(start, end, inp) :
    for i in range(inp) :
        for j in range(i + 1, inp) :
            if(sureForOverlap(start[i], end[i], start[j], end[j])) :
                return True
    return False



# Taking input using Fast I/O for competitive programming
def getInput() :
    inp =  int(input().strip())
    if (inp == 0 ) : 
        temp = input()
        temp = input()
        return list(), list(), inp    
    start = list(map(int, stdin.readline().strip().split(" ")))
    end = list(map(int, stdin.readline().strip().split(" ")))
    return start, end, inp


# Drive functions
if __name__ == '__main__':
    inpt = int(input().strip())
    for i in range(inpt) :
        start, end, n = getInput()
        if(checkForOverlappingIntervals(start, end, n)) :
            print("True")
        else :
            print("False")
