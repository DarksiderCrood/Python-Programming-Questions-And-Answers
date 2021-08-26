'''
Problem Statement
You have been given the start and end times of 'N' intervals. Write a function to check if any two intervals overlap with each other.
Note :
If an interval ends at time T and another interval starts at the same time, they are not considered overlapping intervals.
Input Format :
The first line contains an Integer 'T' which denotes the number of test cases or queries to be run. Then the test cases follow.

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

Time Limit: 1 sec
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
true'''