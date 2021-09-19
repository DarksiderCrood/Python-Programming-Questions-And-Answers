'''
Given two sorted arrays array1 and array2 of size m and n respectively. 
Find the median of the two sorted arrays.

Example 1:

Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5
Example 2:

Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5
Your Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as 
input and returns their median. 

Can you solve the problem in expected time complexity?

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).

Constraints: 
0 ≤ m,n ≤ 104
1 ≤ array1[i], array2[i] ≤ 105
'''

class Solution:
    def MedianOfArrays(self, array1, array2):
        new_arr = sorted(array1 + array2)
        l = len(new_arr)
        
        mid = (l-1)//2
        
        if(l%2==0):
            out = (new_arr[mid] + new_arr[mid+1])/2
            X = int(out)
            temp = out - X
            if (temp > 0):
                return out
            else:
                return int(out)
        
        else:
            return new_arr[mid]
            

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))


# Without Class
array1 = [2]
array2 = [4,1,2]

new_arr = sorted(array1 + array2)
l = len(new_arr)

mid = (l-1)//2

if(l%2==0):
    out = (new_arr[mid] + new_arr[mid+1])/2
    X = int(out)
    temp = out - X
    if (temp > 0):
        print(out)
    else:
        print(int(out))

else:
    print(new_arr[mid])